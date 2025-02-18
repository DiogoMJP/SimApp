import importlib
import json
import os
import sys
from tkinter import filedialog
import tkinter as tk

import Consts
import Page
from data_objects import DataObject
from display_modules import Canvas, StructuredDisplay



class SimApp():
	def __init__(self):
		self.title = Consts.APP_TITLE
		self.width = Consts.APP_WIDTH
		self.height = Consts.APP_HEIGHT

		self.create_window()

		self.open_dir_path = None
		self.open_file_name = None
		self.data = None
		self.call_action = None
		self.pages = {}
		self.active_page= None

		self.window.mainloop()
	

	def create_window(self):
		self.window = tk.Tk()
		self.window.title(self.title)
		self.window.configure(background="white")
		self.window.geometry(str(self.width)+"x"+str(self.height))

		menu = tk.Menu(self.window)
		self.window.config(menu=menu)
		filemenu = tk.Menu(menu)
		menu.add_cascade(label="File", menu=filemenu)
		filemenu.add_command(label="Open File", command=self.open_file)
		filemenu.add_command(label="Close File")
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.window.quit)
		menu.add_command(label="Set Variables", command=self.set_variables_window)
		self.actionmenu = tk.Menu(menu)
		menu.add_cascade(label="Run Action", menu=self.actionmenu)
		popupmenu = tk.Menu(menu)
		helpmenu = tk.Menu(menu)
		menu.add_cascade(label="Help", menu=helpmenu)
		helpmenu.add_command(label="About")
		
		self.frame = tk.Frame(self.window)
		self.frame.pack(expand=True, fill="both")
	

	def open_file(self):
		path = filedialog.askopenfilename(title='Open a File', filetypes=(('SAML File', '.saml'),))
		
		if self.open_dir_path != None:
			sys.path.remove(self.open_dir_path)
		self.open_dir_path = "/".join(path.split("/")[:-1])
		self.open_file_name = path.split("/")[-1]
		sys.path.append(self.open_dir_path)

		with open(path, "r") as file:
			self.data = DataObject.DataObject(json.load(file))
		
		module = importlib.import_module(self.data.get_by_name("launch_file"))
		getattr(module, self.data.get_by_name("launch_function"))(self)
		self.call_action = getattr(module, self.data.get_by_name("call_action_function"))
		for id, data in self.data.get_by_name("pages").get_items():
			self.pages[id] = Page.Page(self, self.frame, data)
		
		self.set_active_page(self.data.get_by_name("starting_page"))

		self.display_self()
	

	def clear_window(self):
		for widget in self.frame.winfo_children():
			widget.destroy()
	
	def set_actions(self):
		self.actionmenu.delete(0, "end")
		actions = self.get_page(self.get_active_page()).get_actions()
		for _, action in actions.get_items():
			self.actionmenu.add_command(label=action.get_by_name("text"),
								command=lambda action=action: self.get_page(self.get_active_page()).call_action(action))


	def get_active_page(self):
		return self.active_page

	def get_page(self, page_name):
		return self.pages[page_name]
	
	def set_display_modules(self, display_modules):
		self.display_modules = DataObject.DataObject(display_modules)
		for key, display_module in self.display_modules.get_items():
			self.display_module_objects[key] = self.display_modules_from_type_string[display_module.get_by_name("type")](self, self.frame, display_module)

	def set_active_page(self, page_name):
		self.active_page = page_name
		self.set_actions()
	
	def display_self(self):
		self.clear_window()
		self.get_page(self.get_active_page()).display_self()
	

	def get_data(self):
		return self.data


	def set_variables_window(self):
		pop_up = tk.Toplevel(self.window)
		pop_up.title("Set Variables")
		pop_up.geometry("400x300")



if __name__ == "__main__":
	App = SimApp()