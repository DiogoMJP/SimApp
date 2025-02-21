from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from data_objects import DataObject
from display_elements import Button, Canvas, Card, TextInput, DisplayElement
if TYPE_CHECKING:
    import Page



class Frame(DisplayElement.DisplayElement):
	"""
	Frame is a class that represents a frame element in a display. It manages the creation, display, and
	manipulation of various display elements within the frame.
	
	Attributes
	----------
	frame : tk.Frame
		the tkinter frame widget that contains the display elements
	display_element_from_type_string : dict
		a dictionary mapping type strings to their corresponding display element classes
	display_elements : dict
		a dictionary storing the display elements by their ids

	Methods
	-------
	get_display_elements_data()
		retrieves the data object containing the layout of display elements
	get_display_element_data(id)
		retrieves the data object for a specific display element by its id
	clear_display_elements()
		clears all display elements from the frame and resets the layout data
	create_display_elements()
		creates display elements based on the layout data
	get_display_elements()
		returns the dictionary of display elements
	get_display_element(id)
		retrieves a specific display element by its id
	append_display_element(id, data)
		appends a new display element to the frame and updates the layout data
	display_self(parent)
		displays the frame and its elements within a given parent tkinter frame
	"""

	def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
		"""
		Initializes the Frame object with the given page and data.

		Arguments
		---------
		page : Page.Page
			the page object to which this frame belongs
		data : data_objects.DataObject.DataObject
			the data object associated with this frame
		"""

		super().__init__(page, data)

		self.frame = None

		self.display_element_from_type_string = {
            "Button" : Button.Button,
			"Canvas" : Canvas.Canvas,
            "Card" : Card.Card,
			"Frame" : Frame,
            "TextInput" : TextInput.TextInput
        }
		self.display_elements = {}

		self.create_display_elements()
	

	def get_display_elements_data(self) -> DataObject.DataObject:
		"""
		Retrieves the display elements data object via its 'layout' id.

		Arguments
		---------
		self : object
			the instance of the class

		Returns
		-------
		data_objects.DataObject.DataObject
			the data object corresponding to the layout ID
		"""

		return self.get_data().get_by_id("layout")
	
	def get_display_element_data(self, id: str) -> DataObject.DataObject:
		"""
		Retrieves the display element data by its id.

		Arguments
		---------
		id : str
			the identifier of the display element

		Returns
		-------
		data_objects.DataObject.DataObject
			the data object associated with the given id
		"""

		return self.get_display_elements_data().get_by_id(id)
	
	def clear_display_elements(self) -> None:
		"""
		Clears all display elements from the frame and resets the layout data.
		"""
		
		for widget in self.frame.winfo_children():
			widget.destroy()
		self.get_data().set_value("layout", {})
		self.display_elements = {}
	
	def create_display_elements(self) -> None:
		"""
		Creates display elements and stores them in the display_elements dictionary.
		It retrieves display elements data, iterates through each item, and creates
		display elements based on their type, storing them in the display_elements
		dictionary.
		"""

		for name, data in self.get_display_elements_data().get_items():
			self.display_elements[name] = \
				self.display_element_from_type_string[data.get_by_id("type")](self.get_page(), data)
	
	def get_display_elements(self) -> dict[str, DisplayElement.DisplayElement]:
		"""
		Retrieves the display elements.

		Returns
		-------
		dict[str, display_elements.DisplayElement.DisplayElement]
			a dictionary containing the display elements
		"""
		
		return self.display_elements
	
	def get_display_element(self, id: str) -> DisplayElement.DisplayElement:
		"""
		Retrieves a display element by its id.

		Arguments
		---------
		id : str
			the identifier of the display element to retrieve

		Returns
		-------
		display_elements.DisplayElement.DisplayElement
			the display element associated with the given identifier
		"""

		return self.get_display_elements()[id]

	def append_display_element(self, id: str, data: (dict | DataObject.DataObject)) -> None:
		"""
		Appends a display element to the current frame.

		Arguments
		---------
		id : str
			unique identifier for the display element
		data : dict | data_objects.DataObject.DataObject
			data associated with the display element
		"""

		if type(data) == dict:
			data = DataObject.DataObject(data)
		self.get_data().get_by_id("layout").set_value(id, data)
		self.display_elements[id] = \
				self.display_element_from_type_string[data.get_by_id("type")](self.get_page(), data)
	

	def display_self(self, parent: tk.Frame) -> None:
		"""
		Displays the frame and its child display elements within the given parent frame.
		
		Arguments
		---------
		parent : tk.Frame
			the parent frame in which this frame will be displayed
		"""

		self.frame = tk.Frame(parent)
		for _, display_element in self.get_display_elements().items():
			display_element.display_self(self.frame)
		self.frame.pack(fill="x")