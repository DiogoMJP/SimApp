from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from data_objects import DataObject
from display_elements import DisplayElement
if TYPE_CHECKING:
    import Page



class TextInput(DisplayElement.DisplayElement):
    def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
        super().__init__(page, data)
        self.label = None
        self.input = None
    

    def display_self(self, parent: tk.Frame) -> None:
        label = self.get_value("label")
        if (label != None):
            self.label = tk.Label(parent, text=label + ":")
            self.label.pack()
        self.input = tk.Entry(parent)
        self.input.bind("<KeyRelease>", self.validate)
        self.input.insert(0, self.get_variable_value())
        self.input.pack()
    

    def validate(self, event: tk.Event) -> None:
        val = self.input.get()

        max_len = self.get_value("max")
        if (max_len != None):
            if len(val) > max_len:
                self.input.delete(0, tk.END)
                self.input.insert(0, val[:max_len])
        self.set_variable(val)