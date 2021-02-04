cipher = "ICE"
cipher_value = bytearray.fromhex(cipher.encode("utf-8").hex())
cipher_length = len(cipher_value)

count = 0
def XOREncrypt(plaintext):
    global count
    hex_value = bytearray.fromhex(plaintext.encode("utf-8").hex())
    final_hex = []
    for v in hex_value:
        xor_result = v ^ cipher_value[count % cipher_length]
        final_hex.append(xor_result)
        count += 1
    encrypted = bytes(final_hex).hex()
    return encrypted

file1 = open("5.txt", "r")
file2 = open("5_encrypted.txt", "w")
file2.write("")

for i, line in enumerate(file1.readlines()):
    if i > 0:
        file2.write("\n")
    encrypted = XOREncrypt(line)
    print("Line {}:\n\t{}\n\t{}".format(i + 1, line, encrypted))
    file2.write(encrypted)

file1.close()
file2.close()