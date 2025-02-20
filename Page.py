import tkinter as tk
from typing import TYPE_CHECKING, Any


from data_objects import DataObject
from display_elements import Button, Card, DisplayElement, Frame, TextInput
if TYPE_CHECKING:
    import SimApp


class Page(object):
	"""
	A class used to represent each page that can be displayed in the application.
	Each Page contains both several typed variables, that store its internal state,
	as well as actions that can be called in the back-end, and a structured layout
	that is displayed to the user.

	Attributes
	----------
	app : SimApp.SimApp
		instance of the SimApp application that "owns" this page 
	parent : tkinter.Frame
		tkinter Frame within which this page's content will be rendered
	data : data_objects.DataObject.DataObject
		instance of DataObject that stores the data corresponding to this page. As this
		object is passed by reference, updating it also results in updating the data
		hierarchy of every other object that contains the corresponding data
	frame : tkinter.Frame
		tkinter Frame that was initialised to represent this page. This Frame has 'parent'
		as its master
	display_element_from_type_string : Dict[str, display_elements.DisplayElement.DisplayElement]
		dictionary that maps the type identifier of each DisplayElement to the
		correspondinng DisplayElement
	display_elements : Dict[str, display_element.DisplayElement.DisplayElement]
		dictionary that maps the id of each display element in this page's layout
		to the corresponding instance of the subclasses of DisplayElement
	
	Methods
	-------
	get_app()
		getter for the 'app' attribute
	get_parent()
		getter for the 'parent' attribute
	get_data()
		getter for the 'data' attribute
	get_variables()
		returns the DataObject with internal state variables stored in 'data'
	get_variable(var_id)
		returns the internal state variable with id 'var_id' stored in 'data'
	get_variable_value(var_id)
		returns the value of the internal state variable with id 'var_id' stored
		in 'data'
	set_variable(var_id, var_val)
		sets the value of the internal state variable 'var_id' as 'var_val'
	call_action(action)
		calls the action 'action' in the back-end
	get_actions()
		returns the DataObject with actions stored in 'data'
	get_action(action_id)
		getter for the action with id 'action_id' stored in 'data'
	get_display_elements_data()
		returns the DataObject with id 'layout' stored in 'data'
	get_display_element_data(display_element_id)
		returns the DataObject with data for the display element with id 'display_element_id'
	clear_display_elements()
		clears all display elements from the page's layout
	create_display_elements()
		initializes DisplayElements based on the data stored in 'data'
	get_display_elements()
		returns a dictionary of all DisplayElements in the page's layout
	get_display_element(id)
		returns the DisplayElement with the specified id
	append_display_element(name, data)
		adds a new display element to the page's layout with the given name and data
	display_self()
		displays the page by creating a tkinter Frame and rendering all display elements within it
	__str__()
		returns a string representation of the page's data
	"""
	
	def __init__(self, app: SimApp.SimApp, parent: tk.Frame, data: DataObject.DataObject) -> None:
		"""
		Parameters
		----------
		app : SimApp.SimApp
			The application instance.
		parent : tk.Frame
			The parent frame in the Tkinter GUI.
		data : data_objects.DataObject.DataObject
			The data object associated with the page.
		"""

		self.app = app
		self.parent = parent
		self.data = data

		self.frame = None

		self.display_element_from_type_string = {
            "Button" : Button.Button,
            "Card" : Card.Card,
			"Frame" : Frame.Frame,
            "TextInput" : TextInput.TextInput
        }
		self.display_elements = {}

		self.create_display_elements()
	

	def get_app(self) -> SimApp.SimApp:
		"""
		Retrieve the SimApp instance associated with this Page.

		Returns
		-------
		SimApp.SimApp
			the application instance associated with this Page.
		"""
		
		return self.app

	def get_parent(self) -> tk.Frame:
		"""
		Retrieves the parent frame of the current widget.
		
		Returns
		-------
		tk.Frame
			the parent frame of the current widget
		"""

		return self.parent
	
	
	def get_data(self) -> DataObject.DataObject:
		"""
		Retrieve the data object associated with this instance.
		
		Returns
		-------
		data_objects. DataObject.DataObject
			the data object stored in this instance
		"""
		
		return self.data

	def get_variables(self) -> DataObject.DataObject:
		"""
		Retrieve the variables from the data.
		
		Returns
		-------
		data_objects.DataObject.DataObject
			a DataObject containing the internal state variables stored in 'data'
		"""

		return self.get_data().get_by_id("vars")

	def get_variable(self, var_id: str) -> DataObject.DataObject:
		"""
		Retrieve a variable by its identifier.

		Arguments
		---------
		var_id : str
			the identifier of the variable to retrieve
		
		Returns
		-------
		data_objects.DataObject.DataObject
			the data object corresponding to the specified variable
		"""

		return self.get_data().get_by_path(["vars", var_id])
	
	def get_variable_value(self, var_id: str) -> DataObject.DataObject:
		"""
		Retrieves the value of a variable by its ID.
		
		Arguments
		---------
		var_id : str
			the ID of the variable to retrieve
		
		Returns
		-------
		DataObject.DataObject
			the value of the variable as a DataObject
		"""
		
		return self.get_data().get_by_path(["vars", var_id, "value"])

	def set_variable(self, var_id: str, var_val: Any) -> None:
		"""
		Sets the value of a variable identified by var_id.

		Arguments
		---------
		var_id : str
			the identifier of the variable to set
		var_val : Any
			the value to assign to the variable
		"""
		
		self.get_data().get_by_id("vars").set_value(var_id, {"name": var_id, "value": var_val, "editable": False})
	

	def call_action(self, action: DataObject.DataObject) -> None:
		"""
		Executes a specified action by retrieving its parameters and calling the corresponding
		application action.
		
		Arguments
		---------
		action : data_objects.DataObject.DataObject
			the action object containing the parameters and id to be executed
		"""
		
		vars = {}
		for v in action.get_by_id("parameters"):
			vars[v] = self.get_variable(v).get_by_id("value")	
		self.get_app().call_action(action.get_by_id("id"), vars)


	def get_actions(self) -> DataObject.DataObject:
		"""
		Retrieves the 'actions' data object from the data source.

		Returns
		-------
		DataObject.DataObject
			the 'actions' DataObject
		"""
		
		return self.get_data().get_by_id("actions")
	
	def get_action(self, action_id: str) -> DataObject.DataObject:
		"""
		Retrieves an action by its id.

		Arguments
		---------
		action_id : str
			the identifier of the action to retrieve

		Returns
		-------
		DataObject.DataObject
			the DataObject corresponding to the specified action ID
		"""

		return self.get_data().get_by_path(["actions", action_id])


	def get_display_elements_data(self) -> DataObject.DataObject:
		"""
		Retrieves the display elements data from this page's layout.

		Returns
		-------
		DataObject.DataObject
			the data object containing the display elements data
		"""

		return self.get_data().get_by_id("layout")
	
	def get_display_element_data(self, display_element_id: str) -> DataObject.DataObject:
		"""
		Retrieves the DataObject associated with a given display element with id 'id'

		Arguments
		---------
		display_element_id : str
			the id of the display element to retrieve data for
		
		Returns
		-------
		DataObject.DataObject
			the data object associated with the given display element id
		"""

		return self.get_display_elements_data().get_by_id(display_element_id)
	
	def clear_display_elements(self) -> None:
		"""
		Clears the page by resetting the layout and display elements.
		"""

		self.get_data().set_value("layout", {})
		self.display_elements = {}
	
	def create_display_elements(self) -> None:
		"""
		Creates DisplayElements based on its layout.
		"""
		
		for name, data in self.get_display_elements_data().get_items():
			self.display_elements[name] = \
				self.display_element_from_type_string[data.get_by_id("type")](self, data)
	
	def get_display_elements(self) -> dict[str, DisplayElement.DisplayElement]:
		"""
		Retrieves the display elements of the page.
		
		Returns
		-------
		dict[str, display_elements.DisplayElement.DisplayElement]
			a dictionary mapping element ids to their corresponding DisplayElement instances
		"""

		return self.display_elements
	
	def get_display_element(self, id: str) -> DisplayElement.DisplayElement:
		"""
		Retrieves a DisplayElement by its id.

		Arguments
		---------
		id : str
			the id of the display element to retrieve
		
		Returns
		-------
		display_elements.DisplayElement.DisplayElement
			the DisplayElement corresponding to the given ID
		"""
		
		return self.get_display_elements()[id]

	def append_display_element(self, id: str, data: (dict | DataObject.DataObject)) -> None:
		"""
		Appends a display element to the display elements dictionary.

		Arguments
		---------
		id : str
			the id of the display element
		data : (dict | DataObject.DataObject)
			the data associated with the display element
		"""

		if type(data) == dict:
			data = DataObject.DataObject(data)
		self.get_data().get_by_id("layout").set_value(id, data)
		self.display_elements[id] = \
			self.display_element_from_type_string[data.get_by_id("type")](self, data)
	

	def __str__(self) -> str:
		"""
		Returns a string representation of the object's data.

		Returns
		-------
		str
			string representation of the data stored in this object
		"""

		return str(self.get_data())


	def display_self(self) -> None:
		"""
		Displays the current object's elements within a new frame.
		This method creates a new frame within the parent widget and displays
		all the elements associated with the current object inside this frame.
		"""

		self.frame = tk.Frame(self.get_parent())
		for _, display_element in self.get_display_elements().items():
			display_element.display_self(self.frame)
		self.frame.pack(expand=True, fill="both")