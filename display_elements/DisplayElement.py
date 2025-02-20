from abc import ABC, abstractmethod



class DisplayElement(ABC):
    def __init__(self, page, data):
        self.page = page
        self.data = data
    

    def get_page(self):
        return self.page


    def get_data(self):
        return self.data

    def get_value(self, var_name):
        return self.get_data().get_by_id(var_name)

    def set_value(self, var_name, value):
        self.get_data().set_value(var_name, value)
    

    def set_variable(self, value):
        self.get_page().set_variable(self.get_value("var"), value)
    

    @abstractmethod
    def display_self(self, parent):
        pass