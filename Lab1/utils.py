import random
import string


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        return data

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def split_string_into_blocks(string, N):
    return [string[i:i+N] for i in range(0, len(string), N)]


def add_padding(block, required_block_size, method_type):
    if method_type == "Space":
        new_block = [' '] * required_block_size
        for i, symbol in enumerate(block):
            new_block[i] = symbol
        return new_block
    if method_type == "Random":
        new_block = [0] * required_block_size
        for i in range(required_block_size):
            if i < len(block):
                new_block[i] = block[i]
            else:
                new_block[i] = random.choice(string.ascii_letters)

def rotate_matrix_right_90(matrix):
    n = len(matrix)
    return [[matrix[n-1-j][i] for j in range(n)] for i in range(n)]

def rotate_matrix_left_90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rotated = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            rotated[i][j] = matrix[j][m - i - 1]
    return rotated