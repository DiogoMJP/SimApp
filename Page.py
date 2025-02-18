import tkinter as tk

from data_objects import DataObject
from display_elements import Button, Card, Frame, TextInput


class Page():
	def __init__(self, app, parent, data : DataObject.DataObject):
		self.app = app
		self.parent = parent
		self.data = data

		self.frame = None

		self.display_element_from_type_string = {
            "Button" : Button.Button,
            "Card" : Card.Card,
			"Frame" : Frame.Frame,
            "TextInput" : TextInput.TextInput
        }
		self.display_elements = {}

		self.create_display_elements()
	

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


	def get_display_elements_data(self):
		return self.get_data().get_by_name("layout")
	
	def get_display_element_data(self, id):
		return self.get_display_elements_data().get_by_name(id)
	
	def clear_display_elements(self):
		self.get_data().set_value("layout", {})
		self.display_elements = {}
	
	def create_display_elements(self):
		for name, data in self.get_display_elements_data().get_items():
			self.display_elements[name] = \
				self.display_element_from_type_string[data.get_by_name("type")](self, data)
	
	def get_display_elements(self):
		return self.display_elements
	
	def get_display_element(self, id):
		return self.get_display_elements()[id]

	def append_display_element(self, name, data):
		if type(data) == dict:
			data = DataObject.DataObject(data)
		self.get_data().get_by_name("layout").set_value(name, data)
		self.display_elements[name] = \
			self.display_element_from_type_string[data.get_by_name("type")](self, data)
	

	def __str__(self):
		return str(self.get_data())


	def display_self(self):
		self.frame = tk.Frame(self.get_parent())
		for _, display_element in self.get_display_elements().items():
			display_element.display_self(self.frame)
		self.frame.pack(expand=True, fill="both")