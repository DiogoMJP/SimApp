from abc import ABC, abstractmethod

from data_objects import DataObject


class DisplayModule(ABC):
	def __init__(self, app, parent, data):
		self.app = app
		self.parent = parent
		self.data = data
	

	def get_app(self):
		return self.app


	def get_parent(self):
		return self.parent
	

	def get_data(self):
		return self.data


	def get_type(self):
		return self.get_data().get_by_id("type")


	def get_variables(self):
		return self.get_data().get_by_id("vars")

	def get_variable(self, var_name):
		return self.get_data().get_by_path(["vars", var_name])
	
	def get_variable_value(self, var_name):
		return self.get_data().get_by_path(["vars", var_name, "value"])

	def set_variable(self, var_name, var_val):
		self.get_data().get_by_id("vars").set_value(var_name, {"name": var_name, "value": var_val, "editable": False})
	

	def call_action(self, action):
		self.get_app().call_action(action, [self.get_variable(v) for v in action.get_by_id("parameters")])


	def get_actions(self):
		return self.get_data().get_by_id("actions")
	
	def get_action(self, action_name):
		return self.get_data().get_by_path(["actions", action_name])


	def get_display_elements(self):
		return self.get_data().get_by_id("display_elements")
	
	def clear_display_elements(self):
		self.get_data().set_value("display_elements", {})
	
	def append_display_element(self, name, display_element):
		if type(display_element) == dict:
			display_element = DataObject.DataObject(display_element)
		self.get_data().get_by_id("display_elements").set_value(name, display_element)
	

	def __str__(self):
		return str(self.get_data())
	

	@abstractmethod
	def display_self(self):
		pass