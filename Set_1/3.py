# XOR cipher: https://en.wikipedia.org/wiki/XOR_cipher

import string

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hex_value = bytearray.fromhex(hex_string)

english_frequency_order = ['e', 'a', 'i', 'u']
fulfilled = []

print("\nFrequencies:")
for character in string.printable:
    xor_against_string = "".join([character.encode("utf-8").hex() for _ in range(len(hex_string))])
    xor_against = bytearray.fromhex(xor_against_string)
    xor_result = bytes(a ^ b for (a, b) in zip(hex_value, xor_against))
    try:
        xor_result_string = xor_result.decode("utf-8").lower()
    except:
        continue
    
    frequencies = []
    for c in english_frequency_order:
        frequency = len(list(filter(lambda x: x==c, xor_result_string))) / len(xor_result_string) * 100
        frequencies.append((c, frequency))
        #frequencies.append(frequency)
        #frequencies[c] = frequency
        # len(list(filter(lambda x: x>0, frequencies))) == len(english_frequency_order)
    
    if set([c for c, f in frequencies if f > 0]) == set(english_frequency_order):
        print("\t{} , {}".format(character, frequencies))
        fulfilled.append((character, xor_result_string))

    ''' # Use dictionary if frequency order matters. For this particular problem, it doesn't.   
    order = [key for key, value in sorted(frequencies.items(), key=lambda a: a[1], reverse=True)]
    if order == english_frequency_order:
        print(character, frequencies)
        fulfilled.append((character, xor_result_string))
    '''
print("\nResults:")
for cipher, ciphertext in fulfilled:
    print("\tCipher: {}\n\t{}\n".format(cipher, ciphertext))

# Cipher: x, X
# Message: cooking mcs like a pound of bacon