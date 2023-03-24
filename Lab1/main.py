import block_cipher
import cardan_cipher
import vigenere_cipher
from cardan_grid import generate_grid, write_grid, generate_random_cells, read_grid
from utils import *
import caesar_cipher

input_file = "input.txt"
output_file  =  "output.txt"
grid_file  =  "grid.txt"

file_content = read_file(input_file)

int_key = 3


# grid = generate_grid(4)
# write_grid(grid, grid_file)
grid = read_grid(grid_file)
processed_text = cardan_cipher.decrypt(file_content, grid)

write_file(output_file, processed_text)