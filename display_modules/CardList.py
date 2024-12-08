import tkinter as tk

from display_modules.DisplayModule import DisplayModule



class CardList(DisplayModule):
    def __init__(self, parent, data):
        super().__init__(parent, data)
