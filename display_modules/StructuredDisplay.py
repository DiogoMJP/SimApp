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
        for element in self.get_display_elements():
            self.display_elements[element["id"]] = self.display_element_from_type_string[element["type"]](self, self.frame, element)
        self.frame.pack()
        print(self.frame)