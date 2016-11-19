
import math
from sympy import * # gives more exact results when using pi/cos/sin etc.

from Node import Node

############## FUNCTIONS ##################
# Returns a list of coordinates in a circle
# r : radius
# n : number of points
def pointsInCircum(r,n=100):
    return [(0,0)] + [(cos(2*pi/n*x)*r,sin(2*pi/n*x)*r) for x in xrange(0,n+1)]

# Returns the Euclidean distance between two Nodes
def distance(node1,node2):
	return math.sqrt(math.pow(node1.x - node2.x,2) + math.pow(node1.y - node2.y,2))

# Returns a fully connected graph of Nodes
# in the shape of a circle, with the center at the origin
def generateGraph(radius=1.0,n=8):
	# Generate points
	points = pointsInCircum(radius,n)

	# Generate nodes
	nodes = [Node(points[i][0],points[i][1],i) for i in range(len(points))]

	# Generate edges
	# Fully connected
	# Edge weight measured by distance between points
	edges = []
	for i in range(len(nodes)):
		row = []
		for j in range(len(nodes)):
			if i == j: # avoid self connections
				row.append(0)
			else:
				row.append(distance(nodes[i],nodes[j]))
		edges.append(row)
	
	return points,nodes,edges

# Plots given points and edges
def plotGraph(points,lines,radius=1.0):
	# Plot points
	x = [p[0] for p in points]
	y = [p[1] for p in points]
	plt.plot(x,y, 'ro')

	# Plot lines
	for r in lines:
		print r[0].idx,r[1].idx
		plt.plot([r[0].x,r[1].x],[r[0].y,r[1].y],'b-',lw=1)

	# Other params for appearance
	size = radius*2
	plt.axis([-size, size, -size, size])
	plt.grid(True)
	plt.axes().set_aspect('equal', 'datalim')

	# Display
	# plt.show()
	return plt
