import dearpygui.dearpygui as dpg


import windows.caesar_cipher_window as caesar_window
import windows.vigenere_cipher_window as vigenere_window
import windows.block_cipher_window as block_window
from Lab1.windows import vigenere_self_cipher_window
from windows import cardan_grid_window, cardan_cipher_window


def button_click(sender, data):
    print(f"Hello, {dpg.get_value('Input 1')} and {dpg.get_value('Input 2')}!")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


# caesar_window.create_window()
# vigenere_window.create_window()
# block_window.create_window() # 0 1 2 10 11 13 14 15 16 12 3 4 5 6 7 8 9 17
cardan_grid_window.create_window()
cardan_cipher_window.create_window()
# vigenere_self_cipher_window.create_window()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()