import dearpygui.dearpygui as dpg

import block_cipher

history = []
def update_history(new_line):
    history.insert(0, new_line)
    dpg.set_value("block_history_tag", "\n".join(history))

def process_callback(sender, data):
    input_text = dpg.get_value("block_input_text")
    key = dpg.get_value("block_input_key")
    try:
        key = process_key(key)
        output = block_cipher.encrypt(input_text, key)
    except Exception as e:
        update_history(f"Error occurred: {e}")

    update_history(f"encrypt: input_text: {input_text}, key: {key}, output: {output}")
    dpg.set_value("block_output_text", output)

def create_window():
    with dpg.window(label="Block cipher"):
        dpg.add_text("Input text:")
        dpg.add_same_line()
        dpg.add_input_text(label="", tag="block_input_text")

        dpg.add_text("Output text:")
        dpg.add_same_line()
        dpg.add_input_text(tag="block_output_text")

        dpg.add_spacing(count=1)
        dpg.add_text("Cipher key:")
        dpg.add_same_line()
        dpg.add_input_text(label="Enter an key", tag="block_input_key")

        dpg.add_spacing(count=1)
        dpg.add_button(label="Process", callback=process_callback)

        dpg.add_spacing(count=1)
        with dpg.child(horizontal_scrollbar=True):
            dpg.add_text("History:")
            dpg.add_input_text(tag="block_history_tag", multiline=True)

def process_key(key: str):
    key = key.strip()
    if "," in key:
        raise Exception("Use spaces as delimiter for input key")

    splited_key = [int(char) for char in key.split(" ")]

    if len(set(splited_key)) != len(splited_key):
        raise Exception("Duplicates occurred in key")

    return splited_key
