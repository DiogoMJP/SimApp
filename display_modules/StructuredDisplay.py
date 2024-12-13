import tkinter as tk

from display_elements import Button, TextInput
from display_modules.DisplayModule import DisplayModule



class StructuredDisplay(DisplayModule):
    def __init__(self, app, parent, data):
        super().__init__(app, parent, data)

        self.display_element_from_type_string = {
            "TextInput" : TextInput.TextInput,
            "Button" : Button.Button
        }
        self.display_elements = {}


    def display_self(self):
        self.frame = tk.Frame(self.parent)
        for name, display_element in self.get_display_elements().get_items():
            self.display_elements[name] = self.display_element_from_type_string[display_element.get_by_name("type")](self, self.frame, display_element)
        self.frame.pack(expand=1, fill="both")