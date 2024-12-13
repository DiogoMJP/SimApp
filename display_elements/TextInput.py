import tkinter as tk

from display_elements import DisplayElement



class TextInput(DisplayElement.DisplayElement):
    def __init__(self, display_module, parent, data):
        super().__init__(display_module, parent, data)
    

    def display_self(self):
        parent = self.get_parent()
        label = self.get_value("label")
        if (label != None):
            self.label = tk.Label(parent, text=label + ":")
            self.label.pack()
        else:
            self.label = None
        self.input = tk.Entry(parent)
        self.input.bind("<KeyRelease>", self.validate)
        self.input.insert(0, self.get_display_module().get_variable_value(self.get_value("var")))
        self.input.pack()
    

    def validate(self, event):
        val = self.input.get()

        max_len = self.get_value("max")
        if (max_len != None):
            if len(val) > max_len:
                self.input.delete(0, tk.END)
                self.input.insert(0, val[:max_len])
        self.set_variable(val)