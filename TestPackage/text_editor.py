import json
import os


package = None


class Package():
	def __init__(self, app):
		self.app = app
		self.actions = {
			"new_text" : self.new_text,
			"delete_text" : self.delete_text,
			"save_text" : self.save_text,
			"exit_editor" : self.exit_editor
		}
	

	def call_action(self, action_name, vars):
		self.actions[action_name](vars)

	def new_text(self, vars):
		self.app.get_data().get_by_path(["pages", "text_editor", "vars", "id"]).set_value("value", vars["id"])
		self.app.get_data().get_by_path(["pages", "text_editor", "vars", "title"]).set_value("value", "")
		self.app.get_data().get_by_path(["pages", "text_editor", "vars", "text"]).set_value("value", "")
		self.app.set_active_page("text_editor")
		self.app.display_self()
		
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
		self.app.get_page("text_list").append_display_element(vars["id"],
			self.get_card_data(vars["id"], vars["title"], vars["text"]))
		self.app.get_data().get_by_path(["pages", "text_list", "vars", "id"]).set_value("value", vars["id"] + 1)
		self.app.set_active_page("text_list")
		self.app.display_self()

	def exit_editor(self, vars):
		pass

	
	def __str__(self):
		return str(self.display_modules)


def launch(app):
	global package
	package = Package(app)


def call_action(action, vars):
	package.call_action(action, vars)