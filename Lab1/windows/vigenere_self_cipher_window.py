import dearpygui.dearpygui as dpg

import vigenere_self_cipher

history = []
def update_history(new_line):
    history.insert(0, new_line)
    dpg.set_value("vigenere_self_history_tag", "\n".join(history))

def process_callback(sender, data):
    decrypt = dpg.get_value("vigenere_self_checkbox_tag")
    input_text = dpg.get_value("vigenere_self_input_text")
    secret_symbol = dpg.get_value("vigenere_self_input_symbol")
    if decrypt:
        output = vigenere_self_cipher.decrypt(input_text, secret_symbol)
        update_history(f"decrypt: input_text: {input_text}, secret_symbol: {secret_symbol}, output: {output}")
    else:
        output = vigenere_self_cipher.encrypt(input_text, secret_symbol)
        print(output)
        update_history(f"encrypt: input_text: {input_text}, secret_symbol: {secret_symbol}, output: {output}")
    dpg.set_value("vigenere_self_output_text", output)

def create_window():
    with dpg.window(label="Vigenere self cipher"):
        dpg.add_text("Input text:")
        dpg.add_same_line()
        dpg.add_input_text(label="", tag="vigenere_self_input_text")

        dpg.add_text("Output text:")
        dpg.add_same_line()
        dpg.add_input_text(tag="vigenere_self_output_text")

        dpg.add_spacing(count=1)
        dpg.add_text("Cipher key:")
        dpg.add_same_line()
        dpg.add_input_text(label="Enter a secret symbol", tag="vigenere_self_input_symbol")

        dpg.add_spacing(count=1)
        dpg.add_button(label="Process", callback=process_callback)
        dpg.add_same_line()
        dpg.add_checkbox(label="Decript", tag="vigenere_self_checkbox_tag")

        dpg.add_spacing(count=1)
        dpg.add_text("History:")


        dpg.add_input_text(tag="vigenere_self_history_tag", multiline=True)


