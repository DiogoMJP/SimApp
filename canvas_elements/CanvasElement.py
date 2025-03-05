from abc import ABC, abstractmethod



class CanvasElement(ABC):
	def __init__(self, page, data):
		self.page = page
		self.data = data
	

	def get_page(self):
		return self.page
	

	def get_data(self):
		return self.data

	def get_value(self, id: str):
		return self.get_data().get_by_id(id)
	

	@abstractmethod
	def display_self(self, canvas, width, height, x, y, zoom):
		pass