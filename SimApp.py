import importlib
import json
import sys
from tkinter import filedialog
import tkinter as tk

import Consts
import Page
from data_objects import DataObject



class SimApp(object):
	"""
	SimApp is a class that represents a simulation application with a graphical user interface (GUI).
	It allows users to open files, set variables, and navigate through different pages of the application.

	Attributes
	----------
	title : str
		the title of the application window
	width : int
		the width of the application window
	height : int
		the height of the application window
	open_dir_path : str or None
		the directory path of the opened file
	open_file_name : str or None
		the name of the opened file
	data : DataObject or None
		the data object loaded from the opened file
	call_action : function or None
		the function to call an action
	pages : dict
		a dictionary of pages in the application
	active_page : str or None
		the currently active page
	window : tk.Tk
		the main application window
	frame : tk.Frame
		the main frame within the application window
	actionmenu : tk.Menu
		the menu for running actions

	Methods
	-------
	create_window()
		creates the main application window and its components
	open_file()
		opens a file dialog to select a file and loads its data
	clear_window()
		clears all widgets from the main frame
	set_actions()
		sets the actions available in the action menu based on the active page
	get_active_page()
		returns the name of the currently active page
	get_page(page_name)
		returns the page object for the given page name
	set_active_page(page_name)
		sets the active page to the given page name and updates the actions
	display_self()
		clears the window and displays the active page
	get_data()
		returns the data object loaded from the opened file
	set_variables_window()
		opens a new window to set variables
	"""
	
	def __init__(self) -> None:
		"""
		Initializes the application with default settings and creates the main window.
		"""

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
	

	def create_window(self) -> None:
		"""
		Creates the main application window with a menu and a frame.
		The window includes a title, background color, and geometry settings.
		It also sets up a menu with options for file operations, setting variables,
		running actions, and accessing help information.
		"""

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
	

	def open_file(self) -> None:
		"""
		Opens a file dialog to select a .saml file, loads its content, and initializes the application
		with the data from the file.
		"""
		
		path = filedialog.askopenfilename(title='Open a File', filetypes=(('SAML File', '.saml'),))
		
		if self.open_dir_path != None:
			sys.path.remove(self.open_dir_path)
		self.open_dir_path = "/".join(path.split("/")[:-1])
		self.open_file_name = path.split("/")[-1]
		sys.path.append(self.open_dir_path)

		with open(path, "r") as file:
			self.data = DataObject.DataObject(json.load(file))
		
		module = importlib.import_module(self.data.get_by_id("launch_file"))
		getattr(module, self.data.get_by_id("launch_function"))(self)
		self.call_action = getattr(module, self.data.get_by_id("call_action_function"))
		for id, data in self.data.get_by_id("pages").get_items():
			self.pages[id] = Page.Page(self, self.frame, data)
		
		self.set_active_page(self.data.get_by_id("starting_page"))

		self.display_self()
	

	def clear_window(self) -> None:
		"""
		Clears all widgets from the frame.
		This method iterates over all child widgets of the frame and destroys them.
		"""

		for widget in self.frame.winfo_children():
			widget.destroy()
	
	def set_actions(self) -> None:
		"""
		Sets the actions for the action menu by retrieving the actions from the active page and adding
		them as commands to the menu.
		"""
		
		self.actionmenu.delete(0, "end")
		actions = self.get_page(self.get_active_page()).get_actions()
		for _, action in actions.get_items():
			self.actionmenu.add_command(label=action.get_by_id("text"),
								command=lambda action=action: self.get_page(self.get_active_page()).call_action(action))


	def get_active_page(self) -> Page.Page:
		"""
		Returns the currently active page in the application.

		Returns
		-------
		Page.Page
			the active page object
		"""
		
		return self.active_page

	def get_page(self, page_id: str) -> Page.Page:
		"""
		Retrieves a Page instance based on the provided page_id.
		
		Arguments
		---------
		page_id : str
			the identifier of the page to retrieve
		
		Returns
		-------
		Page.Page
			the Page object corresponding to the given page_id
		"""
		
		return self.pages[page_id]
	
	def set_active_page(self, page_id: str) -> None:
		"""
		Sets the active page to the given page id and updates the actions accordingly.

		Arguments
		---------
		page_id : str
			the id of the page to be set as active
		"""

		self.active_page = page_id
		self.set_actions()
	
	def display_self(self) -> None:
		"""
		Displays the current active page by clearing the window and invoking the display method of the active page.
		"""

		self.clear_window()
		self.get_page(self.get_active_page()).display_self()
	

	def get_data(self) -> DataObject.DataObject:
		"""
		Retrieves the DataObject associated with this application.

		Returns
		-------
		data_objects.DataObject.DataObject
			the DataObject associated with this instance
		"""

		return self.data


	def set_variables_window(self) -> None:
		"""
		Creates a pop-up window for setting variables
		"""

		pop_up = tk.Toplevel(self.window)
		pop_up.title("Set Variables")
		pop_up.geometry("400x300")



if __name__ == "__main__":
	App = SimApp()