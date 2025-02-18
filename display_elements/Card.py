import tkinter as tk

from display_elements import DisplayElement



class Card(DisplayElement.DisplayElement):
    def __init__(self, page, parent, data):
        super().__init__(page, parent, data)
    

    def display_self(self):
        parent = self.get_parent()
        self.frame = tk.Frame(parent, highlightbackground="black", highlightthickness=1, background="white")
        for _, var in self.get_value("vars").get_items():
            if (label := var.get_by_name("label")) != None:
                label = str(label) + ": "
            else: 
                label = ""
            tk.Label(self.frame, text=label+str(var.get_by_name("value")), background="white").pack()
        self.frame.pack()