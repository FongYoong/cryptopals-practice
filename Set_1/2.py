hex_string = '1c0111001f010100061a024b53535009181c'
hex_value = bytearray.fromhex(hex_string)
against_string = '686974207468652062756c6c277320657965'
against_value = bytearray.fromhex(against_string)
xor_result = bytes(a ^ b for (a, b) in zip(hex_value, against_value))
xor_result_hex = xor_result.hex()
print("Hex string: {}\nAgainst string: {}\nXOR result (Bytes): {}\nXOR result (Hex): {}".format(hex_string, against_string, xor_result, xor_result_hex))