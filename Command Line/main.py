# This method calulates the Manhattan distance between two points.
# The Manhattan distance is calculated by only taking the vertical and horizontal paths.
# This method takes in two tuple values and returns an integer.
# Each tuple represents a point on a grid. The return value is the Manhattan distance between those points
def manhattan_distance(first_point, second_point):
    # Calculate the horizontal distance: | x1 - x2 |
    x_distance = abs(first_point[0] - second_point[0])

    # Calculate the vertical distance: | y1 - y2 |
    y_distance = abs(first_point[1] - second_point[1])

    # Total distance is horizontal distance + vertical distance
    total_distance = x_distance + y_distance

    return total_distance


# This method validates user input to ensure the user is entering integer values for the coordinates.
# This method takes in user input and attempts to cast it to an integer. If the casting is unsuccessful,
# then the method will return false. If casting is successful, this method returns true.
def valid_input(input):
    # Try to convert the input to an int. If this fails, then we return false.
    try:
        int(input)
        return True
    except ValueError:
        return False


# This is the entry point to our program. The main method will continue to ask for user input until
# the user is finished calculating distances.
if __name__ == "__main__":
    print("Please enter two points to calculate the Manhattan distance. Values entered must be integers.")

    while True:
        # Prompt user to enter the x-coordinate for the first point; validate input
        first_x_coord = input("Please enter x-coordinate of first point: ")
        while not valid_input(first_x_coord):
            print("ERROR: Input must be an integer")
            first_x_coord = input("Please enter x-coordinate of first point: ")

        # Prompt user to enter the y-coordinate for the first point; validate input
        first_y_coord = input("Please enter y-coordinate of first point: ")
        while not valid_input(first_y_coord):
            print("ERROR: Input must be an integer")
            first_y_coord = input("Please enter y-coordinate of first point: ")

        # Prompt user to enter the x-coordinate for the second point; validate input
        second_x_coord = input("Please enter x-coordinate of second point: ")
        while not valid_input(second_x_coord):
            print("ERROR: Input must be an integer")
            second_x_coord = input("Please enter x-coordinate of second point: ")

        # Prompt user to enter the y-coordinate for the second point; validate input
        second_y_coord = input("Please enter y-coordinate of second point: ")
        while not valid_input(second_y_coord):
            print("ERROR: Input must be an integer")
            second_y_coord = input("Please enter y-coordinate of second point: ")

        # Create points
        first_point = (int(first_x_coord), int(first_y_coord))
        second_point = (int(second_x_coord), int(second_y_coord))

        # Calculate the manhattan distance and print the value
        result = manhattan_distance(first_point, second_point)
        print("The Manhattan distance is: " + str(result))

        # Jump out of loop if user wishes to exit
        user_input = input("Would you like to calculate another distance? (y/n): ")
        if user_input == "n":
            break