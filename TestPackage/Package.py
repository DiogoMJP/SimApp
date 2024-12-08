import json
import os



class Package():
	def __init__(self, app):
		self.app = app
		self.actions = {
			"new_text" : self.new_text,
			"delete_text" : self.delete_text,
			"save_text" : self.save_text,
			"exit_editor" : self.exit_editor
		}

		self.create_display_modules()


	def create_display_modules(self):
		with open(os.path.dirname(__file__) + "/windows.json", "r") as file:
			self.display_modules = json.load(file)
		self.active_display_module = "Text List"
	
	def get_display_modules(self):
		return self.display_modules
	
	def get_active_display_module(self):
		return self.active_display_module
	

	def call_action(self, action, vars):
		self.actions[action](vars)

	def new_text(self, vars):
		self.display_modules["Text Editor"]["vars"]["id"] = vars[0]
		self.active_display_module = "Text Editor"
		self.app.set_active_display_module("Text Editor")

	def delete_text(self, vars):
		pass

	def save_text(self, vars):
		pass

	def exit_editor(self, vars):
		pass

	
	def __str__(self):
		return str(self.display_modules)