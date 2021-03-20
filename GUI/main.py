from tkinter import *
from tkinter import ttk

def enter_button_click():
    # Get user values
    pointA_x_coor = pointA_x_input.get() 
    pointA_y_coor = pointA_y_input.get()
    pointB_x_coor = pointB_x_input.get() 
    pointB_y_coor = pointB_y_input.get()

    # Create tuples
    pointA = (pointA_x_coor, pointA_y_coor)
    pointB = (pointB_x_coor, pointB_y_coor)

    # Calculate Manhattan distance
    

if __name__ == "__main__":
    # Create main window and give it a title
    root = Tk()
    root.title("Manhattan Distance")

    # Create frame to put inside window (our content will be placed inside this frame)
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create all necessary widgets (this is our content that will be displayed)
    # problem_description: Text label that explains the Manhattan distance
    # user_instructions: Text label that tells the user how to enter values
    problem_description = ttk.Label(mainframe, wraplength=400, text="The Manhattan distance is the distance between two points in a grid (like the grid-like street geography of the New York borough of Manhattan) calculated by only taking a vertical and/or horizontal path.")
    user_instructions = ttk.Label(mainframe, wraplength=400, text="Please enter two points below. \nNote: Value entered must be integers. Any value not specified will result in a 0 for that coordinate.")
    # Point A widgets
    # pointA_label: "Point A"
    # PointA_x_label: "x-coordinate"
    # PointA_y_label: "y-coordinate"
    # pointA_x_input: Input box for Point A x-coordinate
    # pointA_y_input: Input box for Point A y-coordinate
    pointA_label = ttk.Label(mainframe, text="Point A")
    pointA_x_label = ttk.Label(mainframe, text="x-coordinate:")
    pointA_y_label = ttk.Label(mainframe, text="y-coordinate:")
    pointA_x_input = ttk.Entry(mainframe)
    pointA_y_input = ttk.Entry(mainframe)    
    # Point B widgets
    # pointB_label: "Point B"
    # pointB_x_label: "x-coordinate"
    # pointB_y_label: "y-coordinate"
    # pointB_x_input: Input box for Point B x-coordinate
    # pointB_y_input: Input box for Point B y-coordinate
    pointB_label = ttk.Label(mainframe, text="Point B")
    pointB_x_label = ttk.Label(mainframe, text="x-coordinate:")
    pointB_y_label = ttk.Label(mainframe, text="y-coordinate:")
    pointB_x_input = ttk.Entry(mainframe)
    pointB_y_input = ttk.Entry(mainframe)    
    # enter_button: Enter button at the bottom of the window
    enter_button = ttk.Button(mainframe, text="Enter", command=enter_button_click)

    # Place widgets inside frame
    problem_description.grid(column=0, row=0, columnspan=6)
    user_instructions.grid(column=0, row=1, pady=(20,20), columnspan=6)
    pointA_label.grid(column=0, row=3, columnspan=6)
    pointA_x_label.grid(column=0, row=4, sticky=E)
    pointA_x_input.grid(column=1, row=4)
    pointA_y_label.grid(column=0, row=5, sticky=E)
    pointA_y_input.grid(column=1, row=5)
    pointB_label.grid(column=0, row=6, pady=(20,0), columnspan=6)
    pointB_x_label.grid(column=0, row=7, sticky=E)
    pointB_x_input.grid(column=1, row=7)    
    pointB_y_label.grid(column=0, row=8, sticky=E)
    pointB_y_input.grid(column=1, row=8)
    enter_button.grid(column=0, row=9, pady=(20,0) ,columnspan=6)

    # Execute event loop (this will allow our GUI to run continuously)
    root.mainloop()