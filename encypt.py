encryption_mapping = {
    'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J',
    'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R',
    'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z',
    'Y': 'A', 'Z': 'B',
    'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j',
    'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r',
    'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z',
    'y': 'a', 'z': 'b',
    '0': '2', '1': '3', '2': '4', '3': '5', '4': '6',
    '5': '7', '6': '8', '7': '9', '8': '0', '9': '1', "!" : ',', ',' : ".", "." : '!'
    
}

decryption_mapping = {v: k for k, v in encryption_mapping.items()}

def enrypt_string(string):
    result = ''
    for c in string:
        if c in encryption_mapping:
            result += encryption_mapping[c]
        
    return result

def decrypt_string(string):
    result = ''
    for c in string:
        if c in decryption_mapping:
            result += decryption_mapping[c]
        
    return result



