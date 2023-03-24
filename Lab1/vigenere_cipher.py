COUNT_LETTERS_ENG_ALPH = 26

def encrypt(text, key):
    ciphertext = ""
    key = key.upper()
    key_len = len(key)

    i = 0
    while i < len(text):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % key_len]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % COUNT_LETTERS_ENG_ALPH + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % COUNT_LETTERS_ENG_ALPH + ord('a'))
            i += 1
        else:
            text = text[:i] + text[i+1:]
            ciphertext += char

    return ciphertext


def decrypt(text, key):
    plaintext = ""
    key = key.upper()
    key_len = len(key)

    i = 0
    while i < len(text):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % key_len]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % COUNT_LETTERS_ENG_ALPH + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % COUNT_LETTERS_ENG_ALPH + ord('a'))
            i += 1
        else:
            text = text[:i] + text[i + 1:]
            plaintext += char

    return plaintext