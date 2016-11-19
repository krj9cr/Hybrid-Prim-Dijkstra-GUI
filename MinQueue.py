
import sys
from Node import Node

### MinQueue Class ###
# list : stores 'queue' of Nodes
class MinQueue(object):
	def __init__(self,n):
		self.list = n[:]

	def __len__(self):
		return len(self.list)

	# Return true if x is in the queue
	def contains(self,x):
		if x in self.list:
			return True
		return False

	# Return the index of the Node
	# with the minimum key value
	# and remove that Node from the queue
	def extractMin(self):
		min = sys.maxint
		node = None
		for l in self.list:
			if l.key < min:
				min = l.key
				node = l
		self.list.remove(node)
		return node.idx
