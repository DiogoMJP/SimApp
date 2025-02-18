import tkinter as tk

from display_elements import DisplayElement



class Button(DisplayElement.DisplayElement):
    def __init__(self, page, data):
        super().__init__(page, data)
    

    def display_self(self, parent):
        self.input = tk.Button(parent, text=self.get_value("text"), command=self.call_action)
        self.input.pack()


    def call_action(self):
        self.get_page().call_action(self.get_value("on_click"))