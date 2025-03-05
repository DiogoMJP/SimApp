from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from data_objects import DataObject
from display_elements import DisplayElement
if TYPE_CHECKING:
    import Page



class Button(DisplayElement.DisplayElement):
    def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
        super().__init__(page, data)
        self.button = None
    

    def display_self(self, parent: tk.Frame) -> None:
        text = self.get_value("text")
        if text == None:
            text = "Button"

        self.input = tk.Button(parent, text=text, command=self.call_action)
        self.input.pack()