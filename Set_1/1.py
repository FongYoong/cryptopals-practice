import base64

def hexToBase64(hex_string):
    return base64.b64encode(bytearray.fromhex(hex_string))

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
base64_string = hexToBase64(hex_string).decode()
print("Hex: {}\nBase64: {}".format(hex_string, base64_string))

# Base64 applications: https://en.wikipedia.org/wiki/Base64#Other_applications