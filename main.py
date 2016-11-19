# Karen Johnson (krj9cr)

# Python 2.7

# Implementation of Prim's and Dijkstra's algorithms
# Implementation of hybrid of both algorithms
# GUI to control parameters and display graph

import sys
# Tkinter GUI Library
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

from App import *

################# MAIN ####################
def main():
	# Creates a root GUI window and names it
	root = Tk.Tk()
	root.wm_title("Prim & Dijkstra's Algorithms")

	# Creates app
	app = App(root)
	
	# Runs the GUI execution loop
	Tk.mainloop()
	# If you put root.destroy() here, it will cause an error if
	# the window is closed with the window manager.

# Call main if this program is executed alone
if __name__ == "__main__":
	main()

