from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from data_objects import DataObject
from display_elements import DisplayElement
if TYPE_CHECKING:
    import Page



class Button(DisplayElement.DisplayElement):
    """
    Button class represents a button element in the display.

    Attributes
    ----------
    input : tk.Button
        the tkinter button widget

    Methods
    -------
    display_self(parent)
        displays the button on the given parent frame
    call_action()
        calls the action associated with the button click event
    """

    def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
        """
        Initializes a Button object with the given page and data.

        Arguments
        ---------
        page : Page.Page
            the page where the button will be displayed
        data : data_objects.DataObject.DataObject
            the data associated with the button
        """

        super().__init__(page, data)
        self.button = None
    

    def display_self(self, parent: tk.Frame) -> None:
        """
        Displays the button on the given parent frame.

        Arguments
        ---------
        parent : tk.Frame
            the parent frame where the button will be displayed
        """

        self.input = tk.Button(parent, text=self.get_value("text"), command=self.call_action)
        self.input.pack()


    def call_action(self) -> None:
        """
        Triggers the action associated with the button's on_click event by calling the corresponding method on the page.
        """

        self.get_page().call_action(self.get_value("on_click"))