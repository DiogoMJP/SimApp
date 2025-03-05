from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from data_objects import DataObject
from display_elements import DisplayElement
if TYPE_CHECKING:
    import Page



class Card(DisplayElement.DisplayElement):
    def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
        super().__init__(page, data)
        self.frame = None
    

    def display_self(self, parent: tk.Frame) -> None:
        self.frame = tk.Frame(parent, highlightbackground="black", highlightthickness=1, background="white")
        for _, var in self.get_value("vars").get_items():
            if (label := var.get_by_id("text")) != None:
                label = str(label) + ": "
            else: 
                label = ""
            tk.Label(self.frame, text=label+str(var.get_by_id("value")), background="white").pack()
        self.frame.pack(fill="x")