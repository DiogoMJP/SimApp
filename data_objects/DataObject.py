class DataObject():
    def __init__(self, data: dict):
        self.data = {}

        for key, datapoint in data.items():
            if type(datapoint) == dict:
                self.data[key] = DataObject(datapoint)
            else:
                self.data[key] = datapoint


    def get_data(self):
        return self.data


    def get_items(self):
        return self.data.items()


    def get_by_name(self, var_name):
        if var_name in self.data.keys():
            return self.data[var_name]
        else:
            return None


    def get_by_path(self, path):
        if len(path) == 1:
            if path[0] in self.data.keys():
                return self.data[path[0]]
            else:
                return None
        else:
            if path[0] in self.data.keys():
                if type(self.data[path[0]]) == DataObject:
                    return self.data[path[0]].get_by_path(path[1:])
                else:
                    return None
            else:
                return None


    def set_value(self, name, value):
        if type(value) == dict:
            self.data[name] = DataObject(value)
        else:
            self.data[name] = value


    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return str(self.data)