from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter as tk
from typing import TYPE_CHECKING, Any


from data_objects import DataObject
if TYPE_CHECKING:
    import Page



class DisplayElement(ABC):
    """
    DisplayElement is an abstract base class that represents an element to be displayed on a page.
    It manages the association between a page and a data object, and provides methods to get and set
    values within the data object.
    
    Attributes
    ----------
    page : Page.Page
        the page on which the display element is located
    data : data_objects.DataObject.DataObject
        the data object associated with the display element

    Methods
    -------
    get_page()
        returns the Page associated with the display element
    get_data()
        returns the DataObject associated with the display element
    get_value(var_id)
        returns the value associated with the given id 'var' from the data object
    set_value(var_id, value)
        sets the value for the given variable id in the data object
    set_variable(value)
        sets the variable in the page using the value from the data object
    display_self(parent)
        abstract method to display the element on the given parent
    """

    def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
        """
        Initializes a DisplayElement with the given page and data.

        Arguments
        ---------
        page : Page.Page
            the page where the display element will be shown
        data : DataObject.DataObject
            the data object associated with the display element
        """

        self.page = page
        self.data = data
    

    def get_page(self) -> Page.Page:
        """
        Retrieves the page associated with this display element.

        Returns
        -------
        Page.Page
            the page this display element belongs to
        """

        return self.page


    def get_data(self) -> DataObject.DataObject:
        """
        Retrieves the data associated with this display element.

        Returns
        -------
        data_objects.DataObject.DataObject
            the data object associated with this display element
        """
        
        return self.data

    def get_value(self, var_id: str) -> Any:
        """
        Retrieves the value associated with the given variable id.

        Arguments
        ---------
        var_id : str
            the id of the variable to retrieve

        Returns
        -------
        Any
            the value associated with the given variable id
        """
        
        return self.get_data().get_by_id(var_id)

    def set_value(self, var_id: str, value: Any) -> None:
        """
        Sets the value of a variable identified by var_id.

        Arguments
        ---------
        var_id : str
            the identifier of the variable to set
        value : Any
            the value to set for the variable
        """

        self.get_data().set_value(var_id, value)
    

    def set_variable(self, value : Any) -> None:
        """
        Sets a variable on the page to the given value.

        Arguments
        ---------
        value : Any
            the value to set for the variable
        """

        self.get_page().set_variable(self.get_value("var"), value)
    

    @abstractmethod
    def display_self(self, parent : tk.Frame) -> None:
        """
        Displays the element within the given parent frame.
        
        Arguments
        ---------
        parent : tk.Frame
            the parent frame in which the element will be displayed
        """

        pass