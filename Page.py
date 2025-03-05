from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING, Any


from data_objects import DataObject
from display_elements import Button, Canvas, Card, DisplayElement, Frame, TextInput
if TYPE_CHECKING:
    import SimApp


class Page(object):
	def __init__(self, app: SimApp.SimApp, parent: tk.Frame, data: DataObject.DataObject) -> None:
		self.app = app
		self.parent = parent
		self.data = data

		self.frame = None

		self.display_element_from_type_string = {
            "Button" : Button.Button,
			"Canvas" : Canvas.Canvas,
            "Card" : Card.Card,
			"Frame" : Frame.Frame,
            "TextInput" : TextInput.TextInput
        }
		self.display_elements = {}

		self.create_display_elements()
	

	def get_app(self) -> SimApp.SimApp:
		return self.app

	def get_parent(self) -> tk.Frame:
		return self.parent
	
	
	def get_data(self) -> DataObject.DataObject:
		return self.data

	def get_variables(self) -> DataObject.DataObject:
		return self.get_data().get_by_id("vars")

	def get_variable(self, var_id: str) -> DataObject.DataObject:
		return self.get_data().get_by_path(["vars", var_id])
	
	def get_variable_value(self, var_id: str) -> DataObject.DataObject:
		return self.get_data().get_by_path(["vars", var_id, "value"])

	def set_variable(self, var_id: str, var_val: Any) -> None:
		self.get_data().get_by_id("vars").set_value(var_id, {"name": var_id, "value": var_val, "editable": False})
	

	def call_action(self, action: DataObject.DataObject) -> None:
		vars = {}
		for v in action.get_by_id("parameters"):
			vars[v] = self.get_variable(v).get_by_id("value")	
		self.get_app().call_action(action.get_by_id("id"), vars)


	def get_actions(self) -> DataObject.DataObject:
		return self.get_data().get_by_id("actions")
	
	def get_action(self, action_id: str) -> DataObject.DataObject:
		return self.get_data().get_by_path(["actions", action_id])


	def get_display_elements_data(self) -> DataObject.DataObject:
		return self.get_data().get_by_id("layout")
	
	def get_display_element_data(self, display_element_id: str) -> DataObject.DataObject:
		return self.get_display_elements_data().get_by_id(display_element_id)
	
	def clear_display_elements(self) -> None:
		self.get_data().set_value("layout", {})
		self.display_elements = {}
	
	def create_display_elements(self) -> None:
		for name, data in self.get_display_elements_data().get_items():
			self.display_elements[name] = \
				self.display_element_from_type_string[data.get_by_id("type")](self, data)
	
	def get_display_elements(self) -> dict[str, DisplayElement.DisplayElement]:
		return self.display_elements
	
	def get_display_element(self, id: str) -> DisplayElement.DisplayElement:
		return self.get_display_elements()[id]

	def append_display_element(self, id: str, data: (dict | DataObject.DataObject)) -> None:
		if type(data) == dict:
			data = DataObject.DataObject(data)
		self.get_data().get_by_id("layout").set_value(id, data)
		self.display_elements[id] = \
			self.display_element_from_type_string[data.get_by_id("type")](self, data)
	

	def __str__(self) -> str:
		return str(self.get_data())


	def display_self(self) -> None:
		self.frame = tk.Frame(self.get_parent())
		for _, display_element in self.get_display_elements().items():
			display_element.display_self(self.frame)
		self.frame.pack(expand=True, fill="both")