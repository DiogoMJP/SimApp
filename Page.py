import tkinter as tk

from data_objects import DataObject
from display_elements import Button, Card, TextInput


class Page():
	def __init__(self, app, parent, data : DataObject.DataObject):
		self.app = app
		self.parent = parent
		self.data = data

		self.display_element_from_type_string = {
            "Button" : Button.Button,
            "Card" : Card.Card,
            "TextInput" : TextInput.TextInput
        }
		self.display_elements = {}
	

	def get_app(self):
		return self.app

	def get_parent(self):
		return self.parent
	
	
	def get_data(self):
		return self.data

	def get_variables(self):
		return self.get_data().get_by_name("vars")

	def get_variable(self, var_name):
		return self.get_data().get_by_path(["vars", var_name])
	
	def get_variable_value(self, var_name):
		return self.get_data().get_by_path(["vars", var_name, "value"])

	def set_variable(self, var_name, var_val):
		self.get_data().get_by_name("vars").set_value(var_name, {"name": var_name, "value": var_val, "editable": False})
	

	def call_action(self, action):
		vars = {}
		for v in action.get_by_name("parameters"):
			vars[v] = self.get_variable(v).get_by_name("value")	
		self.get_app().call_action(action.get_by_name("id"), vars)


	def get_actions(self):
		return self.get_data().get_by_name("actions")
	
	def get_action(self, action_name):
		return self.get_data().get_by_path(["actions", action_name])


	def get_display_elements(self):
		return self.get_data().get_by_name("layout")
	
	def clear_display_elements(self):
		self.get_data().set_value("layout", {})
	
	def append_display_element(self, name, display_element):
		if type(display_element) == dict:
			display_element = DataObject.DataObject(display_element)
		self.get_data().get_by_name("layout").set_value(name, display_element)
	

	def __str__(self):
		return str(self.get_data())


	def display_self(self):
		self.frame = tk.Frame(self.parent)
		for name, display_element in self.get_display_elements().get_items():
			self.display_elements[name] = self.display_element_from_type_string[display_element.get_by_name("type")](self, self.frame, display_element)
		self.frame.pack(expand=True, fill="both")