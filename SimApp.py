import importlib
import sys
from tkinter import filedialog
import tkinter as tk

from Consts import *
from data_objects import DataObject
from display_modules import Canvas, StructuredDisplay



class SimApp():
	def __init__(self):
		self.title = APP_TITLE
		self.width = APP_WIDTH
		self.height = APP_HEIGHT

		self.create_window()

		self.open_dir_path = None
		self.open_file_name = None
		self.display_modules = None
		self.active_display_module = None
		self.display_module_objects = {}

		self.display_modules_from_type_string = {
			"Canvas" : Canvas.Canvas,
			"StructuredDisplay" : StructuredDisplay.StructuredDisplay
		}

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
		popupmenu.add_cascade(label="Pop Ups", menu=popupmenu)
		tk.Label(popupmenu, text="None Available")
		helpmenu = tk.Menu(menu)
		menu.add_cascade(label="Help", menu=helpmenu)
		helpmenu.add_command(label="About")
		
		self.frame = tk.Frame(self.window)
		self.frame.pack(expand=True, fill="both")
	

	def open_file(self):
		path = filedialog.askopenfilename(title='Open a File', filetypes=(('Python File', '.py'),))
		
		if self.open_dir_path != None:
			sys.path.remove(self.open_dir_path)
		self.open_dir_path = "/".join(path.split("/")[:-1])
		self.open_file_name = path.split("/")[-1]
		sys.path.append(self.open_dir_path)

		module = importlib.import_module(self.open_file_name.split(".")[0])
		self.package = module.Package(self)
		self.display_modules = DataObject.DataObject(self.package.get_display_modules())
		for key, display_module in self.display_modules.get_items():
			self.display_module_objects[key] = self.display_modules_from_type_string[display_module.get_by_name("type")](self, self.frame, display_module)
		self.set_active_display_module(self.package.get_active_display_module())
	

	def clear_window(self):
		for widget in self.frame.winfo_children():
			widget.destroy()
	
	def set_actions(self):
		self.actionmenu.delete(0, "end")
		actions = self.get_active_display_module().get_data().get_by_name("actions")
		for _, action in actions.get_items():
			self.actionmenu.add_command(label=action.get_by_name("label"), command=lambda action=action: self.get_active_display_module().call_action(action))

	def get_active_display_module(self):
		return self.display_module_objects[self.active_display_module]

	def set_active_display_module(self, module_name):
		self.active_display_module = module_name
		self.clear_window()
		self.get_active_display_module().display_self()

		self.set_actions()
	

	def get_data(self):
		return self.display_modules


	def set_variables_window(self):
		pop_up = tk.Toplevel(self.window)
		pop_up.title("Set Variables")
		pop_up.geometry("400x300")
	

	def call_action(self, action, vars):
		self.package.call_action(action, vars)



if __name__ == "__main__":
	App = SimApp()