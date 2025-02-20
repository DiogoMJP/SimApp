from typing import Any



class DataObject(object):
    """
    A class to represent a hierarchical data structure using nested dictionaries.

    Attributes
    ----------
    data : dict
        a dictionary to store the hierarchical data
    
    Methods
    -------
    get_data()
        returns the entire data dictionary
    get_items()
        returns (key, item) tuples for each element in the data dictionary
    get_by_id(id)
        retrieves a value from the data dictionary by its key
    get_by_path(path)
        retrieves a value from the data dictionary by a list of keys representing the path
    set_value(id, value)
        sets a value in the data dictionary
    __str__()
        returns the string representation of the data dictionary
    __repr__()
        returns the string representation of the data dictionary
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes a DataObject instance by recursively converting nested dictionaries into
        DataObject instances.

        Arguments
        ---------
        data : dict
            the input dictionary containing data to be stored in the DataObject instance
        """

        self.data = {}

        for key, datapoint in data.items():
            if type(datapoint) == dict:
                self.data[key] = DataObject(datapoint)
            else:
                self.data[key] = datapoint


    def get_data(self) -> dict:
        """
        Retrieves the data dictionary stored in the object.

        Returns
        -------
        dict
            the data stored in the object
        """

        return self.data


    def get_items(self) -> list[tuple[str, any]]:
        """
        Retrieves the items from the data attribute.
        Returns
        -------
        list[tuple[str, any]]
            a list of tuples containing the key-value pairs from the data attribute
        """
        
        return self.data.items()


    def get_by_id(self, id: str) -> Any:
        """
        Retrieves an item from the data dictionary by its id.

        Arguments
        ---------
        id : str
            the id of the item to retrieve
        
        Returns
        -------
        Any
            the item if found; otherwise None
        """
        
        if id in self.data.keys():
            return self.data[id]
        else:
            return None


    def get_by_path(self, path: list[str]) -> Any:
        """
        Retrieves a value from the data dictionary by following a specified path.

        Arguments
        ---------
        path : list[str]
            list of keys representing the path to the desired value
        
        Returns
        -------
        Any
            the value found at the specified path or None if the path is invalid
        """

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
        """
        Sets the value for a given id in the data dictionary. If the value is a dictionary, it
        is converted to a DataObject.

        Arguments
        ---------
        id : str
            the identifier for the data entry
        value : Any
            the value to be set, can be of any type
        """

        if type(value) == dict:
            self.data[id] = DataObject(value)
        else:
            self.data[id] = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object by calling its __repr__ method.

        Returns
        -------
        str
            string representation of the data object
        """

        return self.__repr__()
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the data object.

        Returns
        -------
        str
            string representation of the data object
        """

        return str(self.data)