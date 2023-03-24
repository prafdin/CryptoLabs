import dearpygui.dearpygui as dpg

import caesar_cipher

history = []
def update_history(new_line):
    history.insert(0, new_line)
    dpg.set_value("history_tag", "\n".join(history))

def process_callback(sender, data):
    decrypt = dpg.get_value("checkbox_tag")
    input_text = dpg.get_value("input_text")
    key = dpg.get_value("input_key")
    if decrypt:
        output = caesar_cipher.decrypt(input_text, key)
        update_history(f"decrypt: input_text: {input_text}, key: {key}, output: {output}")
    else:
        output = caesar_cipher.encrypt(input_text, key)
        update_history(f"encrypt: input_text: {input_text}, key: {key}, output: {output}")
    dpg.set_value("output_text", output)

def create_window():
    with dpg.window(label="Caeser cipher"):
        dpg.add_text("Input text:")
        dpg.add_same_line()
        dpg.add_input_text(label="", tag="input_text")

        dpg.add_text("Output text:")
        dpg.add_same_line()
        dpg.add_input_text(tag="output_text")

        dpg.add_spacing(count=1)
        dpg.add_text("Cipher key:")
        dpg.add_same_line()
        dpg.add_input_int(label="Enter an integer", max_value=100, min_value=0, tag="input_key")

        dpg.add_spacing(count=1)
        dpg.add_button(label="Process", callback=process_callback)
        dpg.add_same_line()
        dpg.add_checkbox(label="Decript", tag="checkbox_tag")

        dpg.add_spacing(count=1)
        dpg.add_text("History:")


        dpg.add_input_text(tag="history_tag", multiline=True)


