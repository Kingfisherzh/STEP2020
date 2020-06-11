import copy

class Node:
	def __init__(self, num):
		self.num = num
		self.followings = []
		# I want to record all of the possibilities of shortest paths,
		# so I use list to record the prev node.
		# prev only be used in BFS
		self.prev = [] 
	def addFollowing(self, node):
		self.followings.append(node)
	def addFollower(self, node):
		self.prev.append(node)

def addFollowing(nodes, names):
	f = open('links.txt')
	lines = f.readlines()
	for line in lines:
		start = line.split("\t")[0]
		end = line.split("\t")[1].replace('\n','')
		nodes[start].addFollowing(nodes[end])
	'''
	for i in nodes:
		print(i, len(nodes[i].followings))
	f.close()
	'''

def createNodes():
	nodes = {}	# num: <class Node>
	namesToNum = {} # name: num
	f = open('nicknames.txt')
	lines = f.readlines()
	for line in lines:
		num = line.split("\t")[0]
		name = line.split("\t")[1].replace('\n','')
		node = Node(num)
		nodes[num] = node
		namesToNum[name] = num
	f.close()	
	return nodes, namesToNum
	

def DeepFirstSearch(target, start, alreadySearched=None, path=None):
	if not path:
		path = []
		path.append(start.num)
	if not alreadySearched:
		alreadySearched = []	# record num

	if start.followings:		
		for node in start.followings:
			if node.num not in alreadySearched:
				if node.num == target.num:
					path.append(node.num)
					print(path)
				else:
					alreadySearched.append(node.num)
					path.append(node.num)
					DeepFirstSearch(target, node, alreadySearched, path)
			else:
				pass

# I want to find out all possible shortest paths
# So I divide queue as two parts, the current layer and the next layer
# Only after go through the current layer, 
# the followings nodes of each node in the current layer will be marked as visited
def BreadthFirstSearch(target, start):
	queue = [[start]]
	visited = [start]
	next_layer = []
	while queue:
		current_layer = queue[0]
		#print('current_layer',[node.num for node in queue[0]])

		if target in current_layer:
			printPath(target)
			break
		elif not current_layer:
			print('No path from', str(start.num), 'to', str(target.num))
			break
		else:
			for node in current_layer:	
				for following in node.followings:
					if (following not in visited) and (following not in current_layer) and (following not in next_layer):
						following.addFollower(node)
						next_layer.append(following)
					elif following in next_layer:
						following.addFollower(node)
				
			visited = visited + [node for node in next_layer]
			queue.append([node for node in next_layer])
			queue.pop(0)
			next_layer.clear()
			

def printPath(target, path=None):
	if not path:
		path = [target]
	if target.prev:
		for prev in target.prev:
			new_path = path.copy()
			new_path.append(prev)
			printPath(prev, new_path)
	else:
		print([node.num for node in path][::-1])


def BFSTest(nodes, names):
	for i in names:
		print(i)
		nodes, names = createNodes()
		addFollowing(nodes, names)
		BreadthFirstSearch(nodes[names['adrian']], nodes[names[i]])


if __name__ == '__main__':
	# nodes:{'1':[<Node>], ...}, names = {'austin':'3'}
	nodes, names = createNodes()
	# read from links.txt
	addFollowing(nodes, names)

	# find adrian, start from austin
	print("DFS results:")
	DeepFirstSearch(nodes[names['adrian']], nodes[names['austin']])
	
	# Single test case
	print("BFS results:")
	# BreadthFirstSearch(nodes[names['adrian']], nodes[names['austin']])

	# Find all shortest paths for every single node towards 1st node 'adrian'
	# Edit it in BFSTest
	BFSTest(nodes, names)