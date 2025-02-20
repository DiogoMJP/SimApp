import tkinter as tk
from typing import TYPE_CHECKING

from data_objects import DataObject
from display_elements import DisplayElement
if TYPE_CHECKING:
    import Page



class Card(DisplayElement.DisplayElement):
    """
    Represents a card element in the display, which is a type of DisplayElement.
    A card is associated with a specific page and data object and can display its elements within a
    parent frame.
    
    Attributes
    ----------
    frame : tk.Frame
        the frame in which the card's elements are displayed
    
    Methods
    -------
    __init__(page, data)
        initializes a Card object with the given page and data
    display_self(parent)
        displays the card's elements within a parent frame
    """
    
    def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
        """
        Initializes a Card object with the given page and data.
        
        Arguments
        ---------
        page : Page.Page
            the page to which the card belongs
        data : DataObject.DataObject
            the data object associated with the card
        """

        super().__init__(page, data)
        self.frame = None
    

    def display_self(self, parent: tk.Frame) -> None:
        """
 
    ""       Displays the card's elements within a parent frame.

        Arguments
        ---------
        parent : tk.Frame
            the parent frame in which the card's elements will be displayed
        """

        self.frame = tk.Frame(parent, highlightbackground="black", highlightthickness=1, background="white")
        for _, var in self.get_value("vars").get_items():
            if (label := var.get_by_id("text")) != None:
                label = str(label) + ": "
            else: 
                label = ""
            tk.Label(self.frame, text=label+str(var.get_by_id("value")), background="white").pack()
        self.frame.pack(fill="x")