import importlib
import sys
from tkinter import filedialog
import tkinter as tk

from Consts import *
from display_modules.Canvas import Canvas



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
		runmenu = tk.Menu(menu)
		menu.add_cascade(label="Run", menu=runmenu)
		runmenu.add_command(label="Run File")
		runmenu.add_command(label="Run and Save File")
		popupmenu = tk.Menu(menu)
		popupmenu.add_cascade(label="Pop Ups", menu=popupmenu)
		tk.Label(popupmenu, text="None Available")
		helpmenu = tk.Menu(menu)
		menu.add_cascade(label="Help", menu=helpmenu)
		helpmenu.add_command(label="About")
	

	def open_file(self):
		path = filedialog.askopenfilename(title='Open a File', filetypes=(('Python File', '.py'),))
		
		if self.open_dir_path != None:
			sys.path.remove(self.open_dir_path)
		self.open_dir_path = "/".join(path.split("/")[:-1])
		self.open_file_name = path.split("/")[-1]
		sys.path.append(self.open_dir_path)

		module = importlib.import_module(self.open_file_name.split(".")[0])
		self.package = module.Package(self)
		self.display_modules = self.package.get_display_modules()
		self.active_display_module = self.package.get_active_display_module()
		print(self.package)


	def set_variables_window(self):
		pop_up = tk.Toplevel(self.window)
		pop_up.title("Set Variables")
		pop_up.geometry("400x300")
	

	def call_action(self, action, parameters, vars):
		self.package.call_action(action, [vars[param] for param in parameters])



if __name__ == "__main__":
	App = SimApp()