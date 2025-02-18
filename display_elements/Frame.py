import tkinter as tk

from data_objects import DataObject
from display_elements import Button, Card, TextInput, DisplayElement



class Frame(DisplayElement.DisplayElement):
	def __init__(self, page, parent, data):
		super().__init__(page, parent, data)

		self.frame = None

		self.display_element_from_type_string = {
            "Button" : Button.Button,
            "Card" : Card.Card,
            "TextInput" : TextInput.TextInput
        }
		self.display_elements = {}
	

	def get_display_elements(self):
		return self.get_data().get_by_name("layout")
	
	def clear_display_elements(self):
		self.get_data().set_value("layout", {})
	
	def append_display_element(self, name, display_element):
		if type(display_element) == dict:
			display_element = DataObject.DataObject(display_element)
		self.get_data().get_by_name("layout").set_value(name, display_element)
	

	def display_self(self):
		self.frame = tk.Frame(self.parent)
		for name, display_element in self.get_display_elements().get_items():
			self.display_elements[name] = self.display_element_from_type_string[display_element.get_by_name("type")](self.page, self.frame, display_element)
		self.frame.pack(expand=True, fill="both")