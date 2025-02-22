import tkinter as tk

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

		self.draw_funcs = {
			"Line" : lambda d : self.draw_line(d.get_by_id("points"), d.get_by_id("fill"), d.get_by_id("dash")),
			"Rectangle" : lambda d : self.draw_rectangle(d.get_by_id("points"), d.get_by_id("fill"))
		}
	
	
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
		for d in self.get_display_elements().get_items():
			self.draw_funcs[d[1].get_by_id("type")](d[1])
	
	def draw_line(self, points, fill="#000", dash=(1, 0)):
		midpoint = (self.width // 2, self.height // 2)
		points = [
			(self.x + midpoint[0] + (x - midpoint[0]) * self.zoom,
			 self.y + midpoint[1] + (y - midpoint[1]) * self.zoom)
			 for x, y in points
		]
		self.canvas.create_line(points, fill=fill, dash=dash)

	def draw_rectangle(self, points, fill="#000"):
		midpoint = (self.width // 2, self.height // 2)
		points = [
			(self.x + midpoint[0] + (x - midpoint[0]) * self.zoom,
			 self.y + midpoint[1] + (y - midpoint[1]) * self.zoom)
			 for x, y in points
		]
		self.canvas.create_rectangle(points, fill=fill)


	def get_display_elements(self):
		return self.get_data().get_by_id("canvas_elements")
	
	def clear_display_elements(self):
		self.get_data().set_value("canvas_elements", {})
	
	def append_display_element(self, name, display_element):
		if type(display_element) == dict:
			display_element = DataObject.DataObject(display_element)
		self.get_data().get_by_id("canvas_elements").set_value(name, display_element)