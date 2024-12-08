import tkinter as tk

from display_modules.DisplayModule import DisplayModule



class StructuredDisplay(DisplayModule):
    def __init__(self, parent, data):
        super().__init__(parent, data)


    def set_window(self):
        frame = tk.Frame(self.parent)
        for element in self.get_display_elements():
            element.render(self)