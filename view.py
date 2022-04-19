import dearpygui.dearpygui as dpg
from controller import Controller


class View:
    def __init__(self, width=600, height=600):
        self.controller = Controller()
        dpg.create_context()
        dpg.create_viewport(title='Workout', width=width, height=height)

        self.__create_menu_bar()
        self.__main_menu()

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Primary Window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()

    def __save_pressed(self):
        print("save")

    def __create_menu_bar(self):
        with dpg.viewport_menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Save", callback=self.__save_pressed)
            with dpg.menu(label="Add"):
                dpg.add_menu_item(label="Weight", callback=self.__add_weight_pressed)
                dpg.add_menu_item(label="Add Workout", tag="add_workout", callback=self.__add_workout_pressed)

    def __add_workout_pressed(self):
        pass

    def __add_weight_pressed(self):
        with dpg.window(tag="Add Weight Window"):
            self._add_weight_input = dpg.add_input_float(tag="new_weight", label="new_weight", default_value=200.0)
            dpg.add_button(tag="add_weight", label="add", callback=self.__save_weight_pressed)

    def __save_weight_pressed(self):
        self.controller.new_weight(dpg.get_value(self._add_weight_input))
        dpg.delete_item("Add Weight Window")

    def __main_menu(self):
        with dpg.window(tag="Primary Window"):
            dpg.add_text("Hello, world")
            save = dpg.add_button(label="Save", callback=self.__save_pressed)
            dpg.add_input_text(label="string", default_value="Quick brown fox")
            dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
