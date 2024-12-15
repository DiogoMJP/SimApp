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
		self.app.set_display_modules(self.get_display_modules())
		self.app.set_active_display_module("Text List")
		self.app.display_active_display_module()


	def create_display_modules(self):
		with open(os.path.dirname(__file__) + "/windows.json", "r") as file:
			self.display_modules = json.load(file)
	
	def get_display_modules(self):
		return self.display_modules
	

	def call_action(self, action, vars):
		self.actions[action.get_by_name("name")](vars)

	def new_text(self, vars):
		self.app.get_data().get_by_path(["Text Editor", "vars", "id"]).set_value("value", vars[0].get_by_name("value"))
		self.app.get_data().get_by_path(["Text Editor", "vars", "title"]).set_value("value", "")
		self.app.get_data().get_by_path(["Text Editor", "vars", "text"]).set_value("value", "")
		self.app.set_active_display_module("Text Editor")
		self.app.display_active_display_module()
		
	def delete_text(self, vars):
		pass

	def get_card_data(self, id, title, text):
		return {
			"name" : id,
			"type" : "Card",
			"vars" : {
				"id": {"name": "id", "label": "ID", "value": id},
				"title": {"name": "title", "label": "Title", "value": title},
				"text": {"name": "text", "label": "Text", "value": text}
			}
		}

	def save_text(self, vars):
		self.app.get_display_module("Text List").append_display_element(vars[0].get_by_name("value"),
			self.get_card_data(vars[0].get_by_name("value"), vars[1].get_by_name("value"), vars[2].get_by_name("value")))
		self.app.get_data().get_by_path(["Text List", "vars", "id"]).set_value("value", vars[0].get_by_name("value") + 1)
		self.app.set_active_display_module("Text List")
		self.app.display_active_display_module()

	def exit_editor(self, vars):
		pass

	
	def __str__(self):
		return str(self.display_modules)