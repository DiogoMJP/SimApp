from abc import ABC, abstractmethod



class DisplayModule(ABC):
	def __init__(self, app, parent, data):
		self.app = app
		self.parent = parent
		self.data = data
	

	def get_app(self):
		return self.app


	def get_parent(self):
		return self.parent


	def get_type(self):
		return self.data["type"]


	def get_variables(self):
		return self.data["vars"]

	def get_variable(self, var_name):
		variable = [var for var in self.data["vars"] if var["name"] == var_name]
		if len(variable) != 0:
			return variable[0]
		else:
			return None
	
	def get_variable_value(self, var_name):
		variable = [var for var in self.data["vars"] if var["name"] == var_name]
		if len(variable) != 0:
			return variable[0]["value"]
		else:
			return None

	def set_variable(self, var_name, var_val):
		for i, _ in enumerate(self.data["vars"]):
			if self.data["vars"][i]["name"] == var_name: 
				self.data["vars"][i]["value"] = var_val
	

	def call_action(self, action):
		self.get_app().call_action(action, [self.get_variable(v) for v in action["parameters"]])


	def get_actions(self):
		return self.data["actions"]
	
	def get_action(self, action_name):
		return self.data["actions"][action_name]


	def get_display_elements(self):
		return self.data["display_elements"]
	
	def clear_display_elements(self):
		self.data["display_elements"] = []
	
	def append_display_element(self, d):
		self.data["display_elements"] += [d]
	

	def __str__(self):
		return str(self.data)
	

	@abstractmethod
	def display_self(self):
		pass