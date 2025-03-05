import tkinter as tk

from canvas_elements import Circle, Line, Rectangle
from data_objects import DataObject
from display_elements import DisplayElement



class Canvas(DisplayElement.DisplayElement):
	def __init__(self, page, data):
		super().__init__(page, data)

		self.width = 300 if self.get_value("width") is None else self.get_value("width")
		self.height = 300 if self.get_value("height") is None else self.get_value("height")

		self.zoom = 1
		self.x = 0
		self.y = 0
		self.start_drag_x = 0
		self.start_drag_y = 0
		self.canvas = None

		self.canvas_element_from_type_string = {
			"Circle": Circle.Circle,
            "Line": Line.Line,
			"Rectangle": Rectangle.Rectangle
        }
		self.canvas_elements = {}

		self.create_canvas_elements()
	
	
	def display_self(self, parent):
		self.canvas = tk.Canvas(parent, width=self.width, height=self.height,
						  bg="white", highlightbackground="black", highlightthickness=1)
		self.canvas.pack()
		self.canvas.bind("<MouseWheel>", self.canvas_zoom)
		self.canvas.bind("<B1-Motion>", self.canvas_drag)
		self.canvas.bind("<Button-1>", self.start_canvas_drag)
		self.render()
	
	def canvas_zoom(self, event):
		if event.num == 5 or event.delta == -120:  # scroll down, smaller
			self.zoom = self.zoom * 0.8
		if event.num == 4 or event.delta == 120:  # scroll up, bigger
			self.zoom = self.zoom * 1.25
		
		self.render()
	
	def start_canvas_drag(self, event):
		self.start_drag_x = event.x
		self.start_drag_y = event.y

	def canvas_drag(self, event):
		self.x = self.x + event.x - self.start_drag_x
		self.y = self.y + event.y - self.start_drag_y
		self.start_drag_x = event.x
		self.start_drag_y = event.y
		self.render()
	
	def render(self):
		self.canvas.delete("all")
		for _, canvas_element in self.get_canvas_elements().items():
			canvas_element.display_self(self.canvas, self.width, self.height, self.x, self.y, self.zoom)

	
	def get_canvas_elements_data(self):
		return self.get_data().get_by_id("canvas_elements")
	
	def get_canvas_element_data(self, id):
		return self.get_canvas_elements_data().get_by_id(id)
	
	def clear_canvas_elements(self):
		for widget in self.frame.winfo_children():
			widget.destroy()
		self.get_data().set_value("canvas_elements", {})
		self.canvas_elements = {}
	
	def create_canvas_elements(self):
		for name, data in self.get_canvas_elements_data().get_items():
			self.canvas_elements[name] = \
				self.canvas_element_from_type_string[data.get_by_id("type")](self.get_page(), data)
	
	def get_canvas_elements(self):
		return self.canvas_elements
	
	def get_canvas_element(self, id):
		return self.get_canvas_elements()[id]

	def append_canvas_element(self, id, data):
		if type(data) == dict:
			data = DataObject.DataObject(data)
		self.get_data().get_by_id("canvas_elements").set_value(id, data)
		self.canvas_elements[id] = \
				self.canvas_element_from_type_string[data.get_by_id("type")](self.get_page(), data)