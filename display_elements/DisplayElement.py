from abc import ABC, abstractmethod



class DisplayElement(ABC):
    def __init__(self, display_module, parent, data):
        self.display_module = display_module
        self.parent = parent
        self.data = data

        self.display_self()
    

    def get_display_module(self):
        return self.display_module
    

    def get_parent(self):
        return self.parent


    def get_data(self):
        return self.data

    def get_value(self, var_name):
        if var_name in self.data.keys():
            return self.data[var_name]
        else:
            return None

    def set_value(self, var_name, value):
        self.data[var_name] = value
    

    def set_variable(self, value):
        self.get_display_module().set_variable(self.get_value("var"), value)
    

    @abstractmethod
    def display_self(self):
        pass