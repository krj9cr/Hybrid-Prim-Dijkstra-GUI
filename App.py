
import sys

# matplotlib libraries
import matplotlib
from matplotlib.figure import Figure

# matplotlib stuff to interact with Tkinter
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# Tkinter GUI Library
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

from Node import Node
from Algorithms import *
from Helpers import *

### App Class ###
# Creates a GUI to display graph and control its params
# master : the parent frame, comes from __main__
# points : current list of generated points 
# nodes  : current list of generated Nodes
# edges  : current list of generated edges
# figure : matplotlib Figure
# canvas : matplotlib canvas that interacts with Tkinter
# plt    : plot of the graph
# radius : current radius
# n      : current number of points
class App:
	def __init__(self, root):
		self.master = root
		self.points = []
		self.nodes  = []
		self.edges  = []

		self.figure = Figure(figsize=(5, 4), dpi=100)
		self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
		self.plt = self.figure.add_subplot(111)

		self.radius = 1.0
		self.n = 8

		# Call setup
		self.setup()

	# Redraws self.plt
	def drawFigure(self,lines,rad=1.0,n=8):
		# Re-generate Graph
		self.points,self.nodes,self.edges = generateGraph(rad,n)

		# Plot points
		x = [p[0] for p in self.points]
		y = [p[1] for p in self.points]
		self.plt.plot(x,y, 'ro')

		# Plot lines
		for r in lines:
			self.plt.plot([r[0].x,r[1].x],[r[0].y,r[1].y],'b-',lw=1)

		# Other params for appearance
		size = rad + 1.0
		self.plt.axis([-size, size, -size, size])
		self.plt.grid(True)

	# Creates the canvas, buttons, and controls for the App
	def setup(self):
		self.plt.clear()
		self.drawFigure([],self.radius,self.n)

		# Algo Buttons
		btnGroup = Tk.Frame(master=self.master)
		btnGroup.pack(side=Tk.RIGHT)

		# Radius
		rad = Tk.StringVar()
		rad.set('1.0')
		rad.trace('w',lambda name, index, mode, sv= rad: self.radiusChanged(rad))
		radEntry = Tk.Entry(master=btnGroup,width=4,textvariable=rad)
		radText = Tk.Label(master=btnGroup,text='Radius:')
		radText.pack(side=Tk.TOP)
		radEntry.pack(side=Tk.TOP)

		# Num points
		numPoints = Tk.StringVar()
		numPoints.set('8')
		numPoints.trace('w',lambda name, index, mode, sv= numPoints: self.nChanged(numPoints))
		npEntry = Tk.Entry(master=btnGroup,width=4,textvariable=numPoints)
		npText = Tk.Label(master=btnGroup,text='Num points:')
		npText.pack(side=Tk.TOP)
		npEntry.pack(side=Tk.TOP)

		# Space
		dummy = Tk.Label(master=btnGroup,text='')
		dummy.pack(side=Tk.TOP)

		# Prim
		primBtn = Tk.Button(master=btnGroup, text='Prim', command=self.primAlgo)
		primBtn.pack(side=Tk.TOP)

		# Dijkstra
		dijkBtn = Tk.Button(master=btnGroup, text='Dijkstra', command=self.dijkAlgo)
		dijkBtn.pack(side=Tk.TOP)

		# Space
		dummy2 = Tk.Label(master=btnGroup,text='')
		dummy2.pack(side=Tk.TOP)

		# Text
		hybridTxt = Tk.Label(master=btnGroup, text='Hybrid:')
		hybridTxt.pack(side=Tk.TOP)

		# Slider
		slider = Tk.Scale(master=btnGroup,from_=0.0,to=1.0,length=150,resolution=0.01,command=self.sliderChanged)
		slider.pack(side=Tk.TOP)

		# Space
		dummy3 = Tk.Label(master=btnGroup,text='')
		dummy3.pack(side=Tk.TOP)

		# Clear
		clearBtn = Tk.Button(master=btnGroup, text='Clear', command=self.clearPlot)
		clearBtn.pack(side=Tk.TOP)

		# Quit Button
		button = Tk.Button(master=btnGroup, text='Quit', command=self._quit)
		button.pack(side=Tk.BOTTOM)

		# Drawing Area
		self.canvas.show()
		self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
		self.canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

		
	# Triggers when the text box for radius is changed
	def radiusChanged(self,sv):
		c = sv.get()[0:4]
		try:
			self.radius = float(c)
			sv.set(c)
		except:
			if c == '':
				self.radius = 0.0
				sv.set('')
			else:
				self.radius = 1.0
				sv.set('1.0')

		self.plt.clear()
		self.drawFigure([],self.radius,self.n)
		self.canvas.show()

	# Triggers when the text box for n is changed
	def nChanged(self,sv):
		c = sv.get()[0:4]
		try:
			self.n = int(c)
			sv.set(c)
		except:
			if c == '':
				self.n = 0
				sv.set('')
			else:
				self.n = 8
				sv.set('8')

		self.plt.clear()
		self.drawFigure([],self.radius,self.n)
		self.canvas.show()

	# Triggers when the slider changes
	def sliderChanged(self,sv):
		try:
			epsilon = float(sv)
			self.hybrAlgo(epsilon)
		except:
			True

	# Triggers on quit
	def _quit(self):
		self.master.quit()     # stops mainloop
		self.master.destroy()  # this is necessary on Windows to prevent
		# Fatal Python Error: PyEval_RestoreThread: NULL tstate

	# Calls Prim
	def primAlgo(self):
		lines = prim(self.nodes[:],self.edges[:])
		self.plt.clear()
		self.drawFigure(lines,self.radius,self.n)
		self.canvas.show()

	# Calls Dijkstra
	def dijkAlgo(self):
		lines = dijkstra(self.nodes[:],self.edges[:])
		self.plt.clear()
		self.drawFigure(lines,self.radius,self.n)
		self.canvas.show()

	# Calls Hybrid
	# not sure what second param is
	def hybrAlgo(self,epsilon):
		lines = hybrid(self.nodes[:],self.edges[:],epsilon)
		self.plt.clear()
		self.drawFigure(lines,self.radius,self.n)
		self.canvas.show()

	# Clears the plot of edges
	def clearPlot(self):
		self.plt.clear()
		self.drawFigure([],self.radius,self.n)
		self.canvas.show()

