COUNT_LETTERS_ENG_ALPH = 26

def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]


        if char.isupper():
            result += chr((ord(char) + s - ord('A')) % COUNT_LETTERS_ENG_ALPH + ord('A'))

        elif char.islower():
            result += chr((ord(char) + s - ord('a')) % COUNT_LETTERS_ENG_ALPH + ord('a'))

        else:
            result += char

    return result

def decrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - s - ord('A')) % COUNT_LETTERS_ENG_ALPH + ord('A'))

        elif char.islower():
            result += chr((ord(char) - s - ord('a')) % COUNT_LETTERS_ENG_ALPH + ord('a'))

        else:
            result += char

    return result

