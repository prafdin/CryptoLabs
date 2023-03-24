import random
import string

from utils import split_string_into_blocks, add_padding


def _encrypt_block(block, key):
    return [block[i] for i in key]

def _decrypt_block(block, key):
    decrypted_block = [0] * len(block)
    for i, j in enumerate(key):
        decrypted_block[j] = block[i]
    return decrypted_block



def encrypt(text, key: list[int], padding_method="Space"):
    if 0 not in key:
        raise Exception('Key should start at 0')
    N = len(key)

    encrypted_text = ""
    for block in split_string_into_blocks(text, N):
        if len(block) < N:
            block = add_padding(block, N, padding_method)
        encrypted_text += "".join(_encrypt_block(block, key))
    return encrypted_text