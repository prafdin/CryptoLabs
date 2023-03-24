import dearpygui.dearpygui as dpg

import vigenere_cipher

history = []
def update_history(new_line):
    history.insert(0, new_line)
    dpg.set_value("vigenere_history_tag", "\n".join(history))

def process_callback(sender, data):
    decrypt = dpg.get_value("vigenere_checkbox_tag")
    input_text = dpg.get_value("vigenere_input_text")
    key = dpg.get_value("vigenere_input_key")
    if decrypt:
        output = vigenere_cipher.decrypt(input_text, key)
        update_history(f"decrypt: input_text: {input_text}, key: {key}, output: {output}")
    else:
        output = vigenere_cipher.encrypt(input_text, key)
        update_history(f"encrypt: input_text: {input_text}, key: {key}, output: {output}")
    dpg.set_value("vigenere_output_text", output)

def create_window():
    with dpg.window(label="Vigenere cipher"):
        dpg.add_text("Input text:")
        dpg.add_same_line()
        dpg.add_input_text(label="", tag="vigenere_input_text")

        dpg.add_text("Output text:")
        dpg.add_same_line()
        dpg.add_input_text(tag="vigenere_output_text")

        dpg.add_spacing(count=1)
        dpg.add_text("Cipher key:")
        dpg.add_same_line()
        dpg.add_input_text(label="Enter an key", tag="vigenere_input_key")

        dpg.add_spacing(count=1)
        dpg.add_button(label="Process", callback=process_callback)
        dpg.add_same_line()
        dpg.add_checkbox(label="Decript", tag="vigenere_checkbox_tag")

        dpg.add_spacing(count=1)
        dpg.add_text("History:")


        dpg.add_input_text(tag="vigenere_history_tag", multiline=True)


