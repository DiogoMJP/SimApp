from typing import Any



class DataObject(object):
    def __init__(self, data: dict) -> None:
        self.data = {}

        for key, datapoint in data.items():
            if type(datapoint) == dict:
                self.data[key] = DataObject(datapoint)
            else:
                self.data[key] = datapoint


    def get_data(self) -> dict:
        return self.data


    def get_items(self) -> list[tuple[str, any]]:
        return self.data.items()


    def get_by_id(self, id: str) -> Any:
        if id in self.data.keys():
            return self.data[id]
        else:
            return None


    def get_by_path(self, path: list[str]) -> Any:
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


    def set_value(self, id: str, value: Any) -> None:
        if type(value) == dict:
            self.data[id] = DataObject(value)
        else:
            self.data[id] = value


    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return str(self.data)