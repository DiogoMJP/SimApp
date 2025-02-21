import tkinter as tk

from display_elements import DisplayElement



class Canvas(DisplayElement.DisplayElement):
	def __init__(self, page, data):
		super().__init__(page, data)
		self.width = 300 if self.get_value("width") is None else self.get_value("width")
		self.height = 300 if self.get_value("height") is None else self.get_value("height")
		self.canvas = None
	
	
	def display_self(self, parent):
		self.canvas = tk.Canvas(parent, width=self.width, height=self.height,
						  bg="white", highlightbackground="black", highlightthickness=1)
		self.canvas.pack()
	# 	self.canvas.bind("<MouseWheel>", self.canvas_zoom)
	# 	self.canvas.bind("<B1-Motion>", self.canvas_drag)
	# 	self.canvas.bind("<Button-1>", self.start_canvas_drag)
	
	# def canvas_zoom(self, event):
	# 	if event.num == 5 or event.delta == -120:  # scroll down, smaller
	# 		self.set_variable("zoom", self.get_variable("zoom") * 0.8)
	# 	if event.num == 4 or event.delta == 120:  # scroll up, bigger
	# 		self.set_variable("zoom", self.get_variable("zoom") * 1.25)
		
	# 	self.render()
	
	# def start_canvas_drag(self, event):
	# 	self.start_drag_x = event.x
	# 	self.start_drag_y = event.y

	# def canvas_drag(self, event):
	# 	self.set_variable_value("x", self.get_variable_value("x") + event.x - self.start_drag_x)
	# 	self.set_variable_value("y", self.get_variable_value("y") + event.y - self.start_drag_y)
	# 	self.start_drag_x = event.x
	# 	self.start_drag_y = event.y
	# 	self.render()