# This is the model class which is responsible for holding user input, performing
# input validation, and calculating the Manhattan distance

from view import *

class Model:
    
    # Initialize the model with necessary variables
    # self.pointA_x_coor: user input for x-coordinate of point A
    # self.pointA_y_coor: user input for y-coordinate of point A
    # self.pointB_x_coor: user input for x-coordinate of point B
    # self.pointB_y_coor: user input for y-coordinate of point B
    # self.point_A: Point A tuple
    # self.point_B: Point B tuple
    def __init__(self):
        self.pointA_x_coor = None
        self.pointA_y_coor = None
        self.pointB_x_coor = None
        self.pointB_y_coor = None
        self.point_A = None
        self.point_B = None

    # This method calculates the Manhattan distance. The Manhattan distance is
    # calculated by subtracting the two x-coordinates, then subtracting the two
    # y-coordinates, then taking the absolute value of each result and adding those
    # two values together. More formally:
    #                       Manhattan Distance = abs(pointA(x-coordinate) - pointB(x-coordinate)) +
    #                                            abs(pointA(y-coordinate) - pointB(y-coordinate))
    def manhattan_distance(self, view):
        # Calculate the horizontal distance: | x1 - x2 |
        x_distance = abs(self.point_A[0] - self.point_B[0])

        # Calculate the vertical distance: | y1 - y2 |
        y_distance = abs(self.point_A[1] - self.point_B[1])

        # Total distance is horizontal distance + vertical distance
        total_distance = x_distance + y_distance

        # Send value to the view
        view.print_result(self.point_A, self.point_B, total_distance)

    # This method validates user input. All values enterted must be integers.
    def valid_input(self, view):
        # Try to cast user values to int. If this fails, print an error.
        try:
            self.pointA_x_coor = int(self.pointA_x_coor)
            self.pointA_y_coor = int(self.pointA_y_coor)
            self.pointB_x_coor = int(self.pointB_x_coor)
            self.pointB_y_coor = int(self.pointB_y_coor)

            # Create point A and point B from coordinates
            self.point_A = (self.pointA_x_coor, self.pointA_y_coor)
            self.point_B = (self.pointB_x_coor, self.pointB_y_coor)

            # Calculate Manhattan distance
            self.manhattan_distance(view)
        except:
            view.invalid_input_error()