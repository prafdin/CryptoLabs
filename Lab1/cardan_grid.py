import random

import numpy as np

from utils import rotate_matrix_right_90


def _create_matrix_size_N(N):
    matrix = [[i+j for j in range(N)] for i in range(1, N*N, N)]
    return matrix


def generate_grid(N):
    eps = 0.1
    if N % 2 == 1:
        raise ValueError("N must be even")
    # if abs((len(open_cells)/(N**2)) - (1/4)) > eps:
    #     raise ValueError("ratio of numbers len(open_cells)/N**2 should be equal 1/4")

    N_small_square = N // 2
    first_matrix = np.array(_create_matrix_size_N(N_small_square))
    second_matrix = np.array(rotate_matrix_right_90(first_matrix))
    third_matrix = np.array(rotate_matrix_right_90(second_matrix))
    fourth_matrix = np.array(rotate_matrix_right_90(third_matrix))

    top_part = np.concatenate((first_matrix, second_matrix), axis=1)
    bottom_part = np.concatenate((fourth_matrix, third_matrix), axis=1)
    grid = np.concatenate((top_part, bottom_part), axis=0)

    count_selected = 0
    selected_numbers = []
    while count_selected != N**2 // 4 :
        random_cell = _random_cell(N-1, N-1)
        number = grid[random_cell]
        if number not in selected_numbers and number != -1:
            selected_numbers.append(number)
            grid[random_cell] = "-1"
            count_selected +=1

    grid[grid > 0] = 0
    grid[grid < 0] = 1
    return grid


def write_grid(grid, file_path):
    with open(file_path, 'w') as f:
        for row in grid:
            f.write('\t'.join(map(str, row)) + '\n')

def grid_to_string(grid):
    return '\n'.join([' '.join([str(cell) for cell in row]) for row in grid])

def read_grid(file_path):
    with open(file_path, 'r') as f:
        return [[int(num) for num in line.split()] for line in f]

def _random_cell(max_x, max_y):
    return (random.randint(0, max_x), random.randint(0, max_y))


def generate_random_cells(count_cells, max_x, max_y):
    cells = []
    while len(cells) < count_cells:
        cell = _random_cell(max_x, max_y)
        if cell not in cells:
            cells.append(cell)

    return cells