from abc import ABC, abstractmethod



class DisplayModule(ABC):
	def __init__(self, parent, data):
		self.parent = parent
		self.data = data
	

	@abstractmethod
	def set_window(self):
		pass


	def get_type(self):
		return self.data["type"]


	def get_variables(self):
		return self.data["vars"]
	
	def get_variable(self, var_name):
		if var_name in self.data["vars"].keys():
			return self.data["vars"][var_name]
		else:
			return None

	def set_variable(self, var_name, var_val):
		self.data["vars"][var_name] = var_val
	

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