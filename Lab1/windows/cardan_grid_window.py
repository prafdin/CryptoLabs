import os.path

import dearpygui.dearpygui as dpg

from cardan_grid import generate_grid, write_grid, grid_to_string

_dir_path= ""

def callback(sender, app_data):
    global _dir_path
    _dir_path = app_data['file_path_name']


def add_file_dialog(sender, data):
    dpg.add_file_dialog(directory_selector=True, callback=callback)

def run_generate_grid(sender, data):
    file_name = dpg.get_value("cardan_grid_file_name_tag")
    if (not file_name):
        dpg.set_value("cardan_grid_output_tag", "Provide file name")
    N = dpg.get_value("cardan_grid_input_key")
    try:
        grid = generate_grid(N)
    except Exception as e:
        dpg.set_value("cardan_grid_output_tag", str(e))

    write_grid(grid, os.path.join(_dir_path, file_name))
    dpg.set_value("cardan_grid_output_tag", grid_to_string(grid))

def create_window():
    with dpg.window(label="Cardan grid"):
        dpg.add_button(label="Select output folder", callback=add_file_dialog)
        dpg.add_input_text(label="File name", tag="cardan_grid_file_name_tag")
        dpg.add_input_int(label="Enter an grid size", max_value=100, min_value=0, tag="cardan_grid_input_key")
        dpg.add_button(label="Generate", callback=run_generate_grid)

        dpg.add_spacing(count=1)
        dpg.add_text("Output")
        dpg.add_input_text(tag="cardan_grid_output_tag", multiline=True)