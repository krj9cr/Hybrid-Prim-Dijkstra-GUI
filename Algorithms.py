
import sys
from Node import Node
from MinQueue import MinQueue

################ PRIM ####################
def prim(nodes,edges):
	# For each vertex, set v.key and v.parent
	for n in nodes:
		n.key = sys.maxint
		n.parent = None

	nodes[0].key = 0
	Q = MinQueue(nodes)

	while len(Q) != 0 :
		u = Q.extractMin()

		for v in range(len(nodes)):
			if v == u:
				continue
			if Q.contains(nodes[v]) and edges[u][v] < nodes[v].key:
				nodes[v].parent = u
				nodes[v].key = edges[u][v] ### IMPORTANT
	result = []
	for n in nodes:
		if n.parent == None:
			continue
		result.append([nodes[n.idx],nodes[n.parent]])
	return result


############## DIJKSTRA ##################
def dijkstra(nodes,edges):
	# For each vertex, set v.key and v.parent
	for n in nodes:
		n.key = sys.maxint
		n.parent = None

	nodes[0].key = 0
	Q = MinQueue(nodes)

	while len(Q) != 0 :
		u = Q.extractMin()

		for v in range(len(nodes)):
			if v == u:
				continue
			val = edges[u][v] + nodes[u].key ### IMPORTANT
			if Q.contains(nodes[v]) and val < nodes[v].key:
				nodes[v].parent = u
				nodes[v].key = val
	# Copy each node and its parent as an edge
	result = []
	for n in nodes:
		if n.parent == None:
			continue
		result.append([nodes[n.idx],nodes[n.parent]])
	return result


############### HYBRID ###################
def hybrid(nodes,edges,epsilon):
	# For each vertex, set v.key and v.parent
	for n in nodes:
		n.key = sys.maxint
		n.parent = None

	nodes[0].key = 0
	Q = MinQueue(nodes)

	while len(Q) != 0 :
		u = Q.extractMin()

		for v in range(len(nodes)):
			if v == u:
				continue
			val = edges[u][v]*epsilon + nodes[u].key*(1.0-epsilon) ### IMPORTANT
			if Q.contains(nodes[v]) and val < nodes[v].key:
				nodes[v].parent = u
				nodes[v].key = val

	# Copy each node and its parent as an edge
	result = []
	for n in nodes:
		if n.parent == None:
			continue
		result.append([nodes[n.idx],nodes[n.parent]])
	return result
