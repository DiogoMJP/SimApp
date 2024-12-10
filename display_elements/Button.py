import tkinter as tk

from display_elements import DisplayElement



class Button(DisplayElement.DisplayElement):
    def __init__(self, display_module, parent, data):
        super().__init__(display_module, parent, data)
    

    def display_self(self):
        parent = self.get_parent()
        self.input = tk.Button(parent, text=self.get_value("text"))
        self.input.pack()