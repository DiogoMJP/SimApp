from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter as tk
from typing import TYPE_CHECKING, Any


from data_objects import DataObject
if TYPE_CHECKING:
    import Page



class DisplayElement(ABC):
    def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
        self.page = page
        self.data = data
    

    def get_page(self) -> Page.Page:
        return self.page


    def get_data(self) -> DataObject.DataObject:
        return self.data

    def get_value(self, var_id: str) -> Any:
        return self.get_data().get_by_id(var_id)

    def set_value(self, var_id: str, value: Any) -> None:
        self.get_data().set_value(var_id, value)

    def get_variable_value(self) -> Any:
        var = self.get_value("var")
        if (var != None):
            return self.get_page().get_variable_value(var)
        else:
            tk.messagebox.showerror("Variable Error", "No variable defined for this element.")
            return None
    

    def set_variable(self, value : Any) -> None:
        var = self.get_value("var")
        if (var != None):
            self.get_page().set_variable(var, value)
        else:
            tk.messagebox.showerror("Variable Error", "No variable defined for this element.")
    

    def call_action(self) -> None:
        action = self.get_value("on_click")
        if (action != None):
            self.get_page().call_action(action)
    

    @abstractmethod
    def display_self(self, parent : tk.Frame) -> None:
        pass