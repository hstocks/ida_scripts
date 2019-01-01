start = 0x6001BC
key = 0x1122334455667788
length = 17576

print("[*] XOR start: {}".format(hex(start)))
for ptr in range(start, start+length, 8): 
    PatchQword(ptr, Qword(ptr) ^ key);

Message("[*] XOR done\n");