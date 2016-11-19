
import sys

### Node Class ###
# x,y    : coordinates in the 2d plane
# i      : unique index/identifier
# key    : min path or cost of edges so far
# parent : previous Node, used to create output edges
class Node(object):
	def __init__(self,x,y,i):
		self.x = x
		self.y = y
		self.idx = i
		self.key = sys.maxint
		self.parent = None

	def __str__(self):
		return str(self.idx) + ': (' + str(self.x) + ',' + str(self.y) + ')'
