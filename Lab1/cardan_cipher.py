import math

import numpy as np
from utils import split_string_into_blocks, add_padding, rotate_matrix_right_90, rotate_matrix_left_90


def _string_to_square_matrix(s, size):
    if size**2 != len(s):
        raise ValueError("Can't convert string to square matrix, not enough lenght of string")
    return  [list(s[i:i+size]) for i in range(0, len(s), size)]



# def encrypt(text, grid, padding_method="Space"):
#     encrypted_text = ""
#     N = len(grid)**2
#     for block in split_string_into_blocks(text, N):
#         if len(block) < N:
#             block = add_padding(block, N, padding_method)
#         block_as_matrix = _string_to_square_matrix(block, int(math.sqrt(N)))
#         for i in range(4):
#             grid_rotated = grid
#             for j in range(i):
#                 grid_rotated = rotate_matrix_90(grid_rotated)
#             mask = np.array(grid_rotated)
#             block_after_apply_mask = np.where(mask, block_as_matrix, '')
#             encrypted_text += ''.join([''.join(row) for row in block_after_apply_mask])
#
#     return encrypted_text

def encrypt(text, grid, padding_method="Space"):
    encrypted_text = ""
    N = len(grid)
    for block in split_string_into_blocks(text, N**2):
        encrypted_matrix = [[""] * N for _ in range(N)]
        if len(block) < N**2:
            block = add_padding(block, N**2, padding_method)
        block = list(block)
        for i in range(4):
            grid_rotated = grid
            for j in range(i):
                grid_rotated = rotate_matrix_right_90(grid_rotated)
            mask = np.array(grid_rotated)
            encrypted_matrix = [
                [block.pop(0) if mask[i][j] else encrypted_matrix[i][j] for j in range(N)] for i in range(N)
            ]
            # for i in range(N):
            #     for j in range(N):
            #         if mask[i][j]:
            #             encrypted_matrix[i][j] = block.pop(0)
        encrypted_text += "".join("".join(map(str, row)) for row in encrypted_matrix)
            # block_after_apply_mask = np.where(mask, part_of_block, '')
            # encrypted_text += ''.join([''.join(row) for row in block_after_apply_mask])

    return encrypted_text


def decrypt(text, grid, padding_method="Space"):
    decrypted_text = ""
    N = len(grid)**2
    for block in split_string_into_blocks(text, N):
        if len(block) < N:
            block = add_padding(block, N, padding_method)
        block_as_matrix = _string_to_square_matrix(block, int(math.sqrt(N)))
        for i in range(4):
            grid_rotated = grid
            for j in range(i):
                grid_rotated = rotate_matrix_right_90(grid_rotated)
            mask = np.array(grid_rotated)
            block_after_apply_mask = np.where(mask, block_as_matrix, '')
            decrypted_text += ''.join([''.join(row) for row in block_after_apply_mask])

    return decrypted_text