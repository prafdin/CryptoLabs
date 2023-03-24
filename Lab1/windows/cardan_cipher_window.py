import dearpygui.dearpygui as dpg

import cardan_cipher
from cardan_grid import read_grid

history = []
def update_history(new_line):
    history.insert(0, new_line)
    dpg.set_value("cardan_cipher_history_tag", "\n".join(history))

def process_callback(sender, data):
    decrypt = dpg.get_value("cardan_cipher_checkbox_tag")
    input_text = dpg.get_value("cardan_cipher_input_text")
    try:
        key_grid = read_grid(_key_file_name)
        if decrypt:
            output = cardan_cipher.decrypt(input_text, key_grid)
            update_history(f"decrypt: input_text: {input_text}, output: {output}")
        else:
            output = cardan_cipher.encrypt(input_text, key_grid)
            update_history(f"encrypt: input_text: {input_text}, output: {output}")
        dpg.set_value("cardan_cipher_output_text", output)
    except Exception as e:
        update_history(f"Error occurred: {e}")

_key_file_name = ""

def select_file_callback(sender, data):
    global _key_file_name
    _key_file_name = next(iter(data['selections'].values()))
    dpg.set_value("cardan_cipher_current_path_tag", _key_file_name)

def select_file_dialog(sender, data):
    with dpg.file_dialog(callback=select_file_callback, directory_selector=False):
        dpg.add_file_extension(".*")

def create_window():
    with dpg.window(label="Cardan cipher"):
        dpg.add_text("Input text:")
        dpg.add_same_line()
        dpg.add_input_text(label="", tag="cardan_cipher_input_text")

        dpg.add_text("Output text:")
        dpg.add_same_line()
        dpg.add_input_text(tag="cardan_cipher_output_text")

        dpg.add_spacing(count=1)
        dpg.add_text("Cipher key:")
        dpg.add_same_line()
        dpg.add_button(label="Select key file", callback=select_file_dialog)
        dpg.add_same_line()
        dpg.add_text(tag="cardan_cipher_current_path_tag")

        dpg.add_spacing(count=1)
        dpg.add_button(label="Process", callback=process_callback)
        dpg.add_same_line()
        dpg.add_checkbox(label="Decript", tag="cardan_cipher_checkbox_tag")

        dpg.add_spacing(count=1)
        dpg.add_text("History:")


        dpg.add_input_text(tag="cardan_cipher_history_tag", multiline=True)


