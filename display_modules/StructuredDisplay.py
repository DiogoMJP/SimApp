import tkinter as tk

from display_elements import Button, Card, TextInput
from display_modules.DisplayModule import DisplayModule



class StructuredDisplay(DisplayModule):
    def __init__(self, app, parent, data):
        super().__init__(app, parent, data)

        self.display_element_from_type_string = {
            "Button" : Button.Button,
            "Card" : Card.Card,
            "TextInput" : TextInput.TextInput
        }
        self.display_elements = {}


    def display_self(self):
        self.frame = tk.Frame(self.parent)
        for name, display_element in self.get_display_elements().get_items():
            self.display_elements[name] = self.display_element_from_type_string[display_element.get_by_id("type")](self, self.frame, display_element)
        self.frame.pack(expand=1, fill="both")