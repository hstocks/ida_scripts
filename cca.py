from idaapi import *

def closest_common_ancestor(a, b, max_depth):
	a_anc = []

	nodes = [get_func_name(a)]
	done = []

	# Construct ancestors of a
	while nodes:
		orig_len = len(nodes)
		for n in range(0, len(nodes)):
			if nodes[n] not in a_anc:
				a_anc.append(nodes[n])

			# Add all xrefs to node
			func_addr = get_name_ea_simple(nodes[n])

			for x in XrefsTo(func_addr):
				name = get_func_name(x.frm)
				if name and name not in nodes:
					nodes.append(name)

		nodes = nodes[orig_len:]


	nodes = [get_func_name(b)]
	while nodes:
		orig_len = len(nodes)
		for n in range(0, len(nodes)):
			if nodes[n] in a_anc:
				return nodes[n]

			# Add all xrefs to node
			func_addr = get_name_ea_simple(nodes[n])

			for x in XrefsTo(func_addr):
				name = get_func_name(x.frm)
				if name and name not in nodes:
					nodes.append(name)

		nodes = nodes[orig_len:]

	return None


a = AskLong(0, "Function A: ")
b = AskLong(0, "Function B: ")
cca = closest_common_ancestor(a, b, 0)
print("[*] Closest common ancestor: {}".format(cca))