from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from data_objects import DataObject
from display_elements import Button, Canvas, Card, TextInput, DisplayElement
if TYPE_CHECKING:
    import Page



class Frame(DisplayElement.DisplayElement):
	def __init__(self, page: Page.Page, data: DataObject.DataObject) -> None:
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
		return self.get_data().get_by_id("layout")
	
	def get_display_element_data(self, id: str) -> DataObject.DataObject:
		return self.get_display_elements_data().get_by_id(id)
	
	def clear_display_elements(self) -> None:
		for widget in self.frame.winfo_children():
			widget.destroy()
		self.get_data().set_value("layout", {})
		self.display_elements = {}
	
	def create_display_elements(self) -> None:
		for name, data in self.get_display_elements_data().get_items():
			self.display_elements[name] = \
				self.display_element_from_type_string[data.get_by_id("type")](self.get_page(), data)
	
	def get_display_elements(self) -> dict[str, DisplayElement.DisplayElement]:
		return self.display_elements
	
	def get_display_element(self, id: str) -> DisplayElement.DisplayElement:
		return self.get_display_elements()[id]

	def append_display_element(self, id: str, data: (dict | DataObject.DataObject)) -> None:
		if type(data) == dict:
			data = DataObject.DataObject(data)
		self.get_data().get_by_id("layout").set_value(id, data)
		self.display_elements[id] = \
				self.display_element_from_type_string[data.get_by_id("type")](self.get_page(), data)
	

	def display_self(self, parent: tk.Frame) -> None:
		self.frame = tk.Frame(parent)
		for _, display_element in self.get_display_elements().items():
			display_element.display_self(self.frame)
		self.frame.pack(fill="x")