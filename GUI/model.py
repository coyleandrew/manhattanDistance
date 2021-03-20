from view import *

class Model:
    def __init__(self):
        self.pointA_x_coor = None
        self.pointA_y_coor = None
        self.pointB_x_coor = None
        self.pointB_y_coor = None
        self.point_A = None
        self.point_B = None

    def manhattan_distance(self, view):
        # Calculate the horizontal distance: | x1 - x2 |
        x_distance = abs(self.point_A[0] - self.point_B[0])

        # Calculate the vertical distance: | y1 - y2 |
        y_distance = abs(self.point_A[1] - self.point_B[1])

        # Total distance is horizontal distance + vertical distance
        total_distance = x_distance + y_distance

        # Send value to the view
        view.print_result(self.point_A, self.point_B, total_distance)


    def valid_input(self, view):
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