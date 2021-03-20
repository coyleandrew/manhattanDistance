# This file contains the main method which is the entry point into our program

from controller import *

if __name__ == "__main__":
    controller = Controller() 
    controller.view.root.mainloop()