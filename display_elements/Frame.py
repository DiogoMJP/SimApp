import tkinter as tk

from data_objects import DataObject
from display_elements import Button, Card, TextInput, DisplayElement



class Frame(DisplayElement.DisplayElement):
	def __init__(self, page, data):
		super().__init__(page, data)

		self.frame = None

		self.display_element_from_type_string = {
            "Button" : Button.Button,
            "Card" : Card.Card,
			"Frame" : Frame,
            "TextInput" : TextInput.TextInput
        }
		self.display_elements = {}

		self.create_display_elements()
	

	def get_display_elements_data(self):
		return self.get_data().get_by_name("layout")
	
	def get_display_element_data(self, id):
		return self.get_display_elements_data().get_by_name(id)
	
	def clear_display_elements(self):
		for widget in self.frame.winfo_children():
			widget.destroy()
		self.get_data().set_value("layout", {})
		self.display_elements = {}
	
	def create_display_elements(self):
		for name, data in self.get_display_elements_data().get_items():
			self.display_elements[name] = \
				self.display_element_from_type_string[data.get_by_name("type")](self.get_page(), data)
	
	def get_display_elements(self):
		return self.display_elements
	
	def get_display_element(self, id):
		return self.get_display_elements()[id]

	def append_display_element(self, name, data):
		if type(data) == dict:
			data = DataObject.DataObject(data)
		self.get_data().get_by_name("layout").set_value(name, data)
		self.display_elements[name] = \
				self.display_element_from_type_string[data.get_by_name("type")](self.get_page(), data)
	

	def display_self(self, parent):
		self.frame = tk.Frame(parent)
		for _, display_element in self.get_display_elements().items():
			display_element.display_self(self.frame)
		self.frame.pack(fill="x")