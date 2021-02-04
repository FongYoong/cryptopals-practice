def HammingDistance(string1, string2):
    if len(string1) != len(string2):
        raise Exception("Lengths of strings are not equal")
    string1_hex_value = bytearray.fromhex(string1.encode("utf-8").hex())
    string2_hex_value = bytearray.fromhex(string2.encode("utf-8").hex())
    xor_result = bytes(a ^ b for (a, b) in zip(string1_hex_value, string2_hex_value))
    distance = 0
    for byte in xor_result:
        for bit in bin(byte)[2:]:
            if bit == '1':
                distance += 1
    return distance

distance = HammingDistance("this is a test", "wokka wokka!!!")