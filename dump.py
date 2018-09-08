# Dump n bytes from the current location
import sys

start = ScreenEA()
n = AskLong(0, "How many bytes would you like to dump from address {}?".format(hex(start)))
fname = AskStr("C:\\Users\\user\\Documents\\", "Output file:")

sys.stdout.write("[*] Dumping {} bytes from {} to {}...".format(n, hex(start), fname))
with open(fname, "wb") as f:
	for i in range(0, n):
		b = Byte(start + i)
		f.write(chr(b))

print(" done.")