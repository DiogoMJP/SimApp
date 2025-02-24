from canvas_elements import CanvasElement



class Rectangle(CanvasElement.CanvasElement):
	def __init__(self, page, data):
		super().__init__(page, data)


	def display_self(self, canvas, width, height, canvas_x, canvas_y, zoom):
		midpoint = (width // 2, height // 2)
		points = [
			(canvas_x + midpoint[0] + (x - midpoint[0]) * zoom,
			 canvas_y + midpoint[1] + (y - midpoint[1]) * zoom)
			 for x, y in self.get_value("points")
		]
		fill = self.get_value("fill"),
		canvas.create_rectangle(points, fill=fill)