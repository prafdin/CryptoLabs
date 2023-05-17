from Lab1 import vigenere_cipher

COUNT_LETTERS_ENG_ALPH = 26

# def encrypt(text):
#     ciphertext = ''
#     for i in range(len(text)):
#         char = text[i]
#         key_symbol = text[i-1] if i > 0 else text[-1]
#         if key_symbol.isupper():
#             shift = ord(key_symbol) - ord('A')
#         else:
#             shift = ord(key_symbol) - ord('a')
#         if char.isupper():
#             ciphertext += chr((ord(text[i]) - ord('A') + shift) % COUNT_LETTERS_ENG_ALPH + ord('A'))
#         else:
#             ciphertext += chr((ord(text[i]) - ord('a') + shift) % COUNT_LETTERS_ENG_ALPH + ord('a'))
#
#     return ciphertext

def encrypt(text, secret_symbol):
    return vigenere_cipher.encrypt(text, secret_symbol + text[:-1])


def decrypt(text, secret_symbol):
    key = "" + secret_symbol
    key = key.upper()
    plaintext = ""
    i = 0
    while i < len(text):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i]) - ord('A')
            print(shift)
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % COUNT_LETTERS_ENG_ALPH + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % COUNT_LETTERS_ENG_ALPH + ord('a'))
            key += decrypted_char
            key = key.upper()
            plaintext += decrypted_char
            i += 1
        else:
            text = text[:i] + text[i + 1:]
            plaintext += char

    return plaintext

# def decrypt(ciphertext):
#     plaintext = ''
#     for i in range(len(ciphertext)):
#         char = ciphertext[i]
#         key_symbol = ciphertext[i - 1] if i > 0 else ciphertext[-1]
#         if key_symbol.isupper():
#             shift = ord(key_symbol) - ord('A')
#         else:
#             shift = ord(key_symbol) - ord('a')
#         if char.isupper():
#             plaintext += chr((ord(ciphertext[i]) - ord('A') - shift) % COUNT_LETTERS_ENG_ALPH + ord('A'))
#         else:
#             plaintext += chr((ord(ciphertext[i]) - ord('a') - shift) % COUNT_LETTERS_ENG_ALPH + ord('a'))
#
#     return plaintext