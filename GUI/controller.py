# This is the controller class that is responsible for taking in user input
# and sending it to the model

from tkinter import *
from tkinter import ttk
from view import *
from model import *

class Controller:

    # This method is responsible for creating a controller object.
    # The controller object then instantiates the model and the view
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    # This method is responsible for handling the user input when they
    # press the 'Enter' button on the GUI. The user input is taken from
    # the view and given to the model. The user input is then validated
    # by the model.
    def enter_button_click(self):
        # Get user values
        self.model.pointA_x_coor = self.view.pointA_x_input.get()
        self.model.pointA_y_coor = self.view.pointA_y_input.get()
        self.model.pointB_x_coor = self.view.pointB_x_input.get()
        self.model.pointB_y_coor = self.view.pointB_y_input.get()

        # Validate user input (all values must be integers)
        self.model.valid_input(self.view)
