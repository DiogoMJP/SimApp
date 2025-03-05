from canvas_elements import CanvasElement



class Circle(CanvasElement.CanvasElement):
	def __init__(self, page, data):
		super().__init__(page, data)
	

	def display_self(self, canvas, width, height, canvas_x, canvas_y, zoom):
		midpoint = (width // 2, height // 2)
		center = self.get_value("center")
		radius = self.get_value("radius")
		points = [
			(midpoint[0] + (canvas_x + center[0] - radius) * zoom,
	            midpoint[1] + (canvas_y + center[1] - radius) * zoom),
			(midpoint[0] + (canvas_x + center[0] + radius) * zoom,
	            midpoint[1] + (canvas_y + center[1] + radius) * zoom)
		]
		fill = self.get_value("fill"),
		dash = self.get_value("dash")
		canvas.create_oval(points, fill=fill, dash=dash, width=1*zoom)