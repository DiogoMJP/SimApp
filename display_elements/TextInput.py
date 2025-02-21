from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from data_objects import DataObject
from display_elements import DisplayElement
if TYPE_CHECKING:
    import Page



class TextInput(DisplayElement.DisplayElement):
    """
    TextInput is a class that represents a text input field in a graphical user interface. It inherits
    from DisplayElement and provides functionality to display a label and an input field, validate the
    input, and update the associated data object.
    
    Attributes
    ----------
    label : tk.Label | None
        the label widget associated with the text input field
    input : tk.Entry | None
        the entry widget for user input
    
    Methods
    -------
    display_self(parent)
        displays the text input field and its label on the given parent frame
    validate(event)
        validates the input and updates the associated variable
    """

    def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
        """
        Initializes the TextInput object with the given page and data.

        Arguments
        ---------
        page : Page.Page
            the page where the text input will be displayed
        data : data_objects.DataObject.DataObject
            the data object associated with the text input
        """

        super().__init__(page, data)
        self.label = None
        self.input = None
    

    def display_self(self, parent: tk.Frame) -> None:
        """
        Displays the text input element within the given parent frame. If a label is provided, it
        will be displayed above the input field.

        Arguments
        ---------
        parent : tk.Frame
            the parent frame in which the text input element will be displayed
        """

        label = self.get_value("label")
        if (label != None):
            self.label = tk.Label(parent, text=label + ":")
            self.label.pack()
        else:
            self.label = None
        self.input = tk.Entry(parent)
        self.input.bind("<KeyRelease>", self.validate)
        self.input.insert(0, self.get_page().get_variable_value(self.get_value("var")))
        self.input.pack()
    

    def validate(self, event: tk.Event) -> None:
        """
        Validates the input text length and updates the input field if necessary.

        Arguments
        ---------
        event : tk.Event
            the event that triggered the validation
        """

        val = self.input.get()

        max_len = self.get_value("max")
        if (max_len != None):
            if len(val) > max_len:
                self.input.delete(0, tk.END)
                self.input.insert(0, val[:max_len])
        self.set_variable(val)