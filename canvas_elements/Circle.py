from canvas_elements import CanvasElement



class Circle(CanvasElement.CanvasElement):
	def __init__(self, page, data):
		super().__init__(page, data)
	

	def display_self(self, canvas, width, height, canvas_x, canvas_y, zoom):
		midpoint = (width // 2, height // 2)
		center = self.get_value("center")
		radius = self.get_value("radius")
		points = [
			(canvas_x + midpoint[0] + (center[0] - radius - midpoint[0]) * zoom,
	            canvas_y + midpoint[1] + (center[1] - radius - midpoint[1]) * zoom),
			(canvas_x + midpoint[0] + (center[0] + radius - midpoint[0]) * zoom,
	            canvas_y + midpoint[1] + (center[1] + radius - midpoint[1]) * zoom)
		]
		fill = self.get_value("fill"),
		dash = self.get_value("dash")
		canvas.create_oval(points, fill=fill, dash=dash)