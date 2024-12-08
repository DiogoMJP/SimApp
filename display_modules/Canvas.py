import tkinter as tk

from display_modules.DisplayModule import DisplayModule



class Canvas(DisplayModule):
	def __init__(self, parent, data):
		super().__init__(parent, data)

		self.set_window()

		self.width = 800
		self.height = 600
		self.start_drag_x = 0
		self.start_drag_y = 0

		self.set_variable("zoom", 1)
		self.set_variable("x", 0)
		self.set_variable("y", 0)

		self.draw_funcs = {
			"line" : lambda d : self.draw_line(d["points"], d["fill"], d["dash"]),
			"rect" : lambda d : self.draw_rectangle(d["points"], d["fill"])
		}
	
	def set_window(self):
		self.canvas = tk.Canvas(self.parent)
		self.canvas.pack(fill="both", expand=1)
		self.canvas.bind("<MouseWheel>", self.canvas_zoom)
		self.canvas.bind("<B1-Motion>", self.canvas_drag)
		self.canvas.bind("<Button-1>", self.start_canvas_drag)
	

	def canvas_zoom(self, event):
		if event.num == 5 or event.delta == -120:  # scroll down, smaller
			self.set_variable("zoom", self.get_variable("zoom") * 0.8)
		if event.num == 4 or event.delta == 120:  # scroll up, bigger
			self.set_variable("zoom", self.get_variable("zoom") * 1.25)
		
		self.render()
	
	def start_canvas_drag(self, event):
		self.start_drag_x = event.x
		self.start_drag_y = event.y

	def canvas_drag(self, event):
		self.set_variable("x", self.get_variable("x") + event.x - self.start_drag_x)
		self.set_variable("y", self.get_variable("y") + event.y - self.start_drag_y)
		self.start_drag_x = event.x
		self.start_drag_y = event.y
		self.render()

	
	def draw_line(self, points, fill="#000", dash=(1, 0)):
		midpoint = (self.width // 2, self.height // 2)
		points = [
			(self.get_variable("x") + midpoint[0] + (x - midpoint[0]) * self.get_variable("zoom"),
			 self.get_variable("y") + midpoint[1] + (y - midpoint[1]) * self.get_variable("zoom"))
			 for x, y in points
		]
		self.canvas.create_line(points, fill=fill, dash=dash)

	def draw_rectangle(self, points, fill="#000"):
		midpoint = (self.width // 2, self.height // 2)
		points = [
			(self.get_variable("x") + midpoint[0] + (x - midpoint[0]) * self.get_variable("zoom"),
			 self.get_variable("y") + midpoint[1] + (y - midpoint[1]) * self.get_variable("zoom"))
			 for x, y in points
		]
		self.canvas.create_rectangle(points, fill=fill)
	

	def render(self):
		self.canvas.delete("all")
		for d in self.get_display_elements():
			self.draw_funcs[d["type"]](d)