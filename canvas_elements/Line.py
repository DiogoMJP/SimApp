from canvas_elements import CanvasElement



class Line(CanvasElement.CanvasElement):
	def __init__(self, page, data):
		super().__init__(page, data)
	

	def display_self(self, canvas, width, height, canvas_x, canvas_y, zoom):
		midpoint = (width // 2, height // 2)
		points = [
			(midpoint[0] + (canvas_x + x) * zoom,
			 midpoint[1] + (canvas_y + y) * zoom)
			 for x, y in self.get_value("points")
		]
		fill = self.get_value("fill"),
		dash = self.get_value("dash")
		canvas.create_line(points, fill=fill, dash=dash)