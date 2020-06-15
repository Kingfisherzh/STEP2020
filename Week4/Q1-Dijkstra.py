

def Dijkstra(node_dist, current_node, target):
	not_visited = [_ for _ in range(num_station)]
	shortest_dist = [999 for _ in range(num_station)]		# Initialize the distance
	shortest_path = [[] for _ in range(num_station)]		# Record paths
	shortest_dist[int(current_node)] = 0					# Distance from start node is 0

	while not_visited:
		if current_node in not_visited:
			if node_dist[str(current_node)]:
				for node in node_dist[str(current_node)].keys():
					if shortest_dist[int(node)] > shortest_dist[current_node] + node_dist[str(current_node)][node]:
						shortest_dist[int(node)] = shortest_dist[current_node] + node_dist[str(current_node)][node]
						for prev_node in shortest_path[int(current_node)]:
							shortest_path[int(node)].append(prev_node)
						shortest_path[int(node)].append(str(current_node))
				
			shortest_copy = shortest_dist.copy()	
			not_visited.remove(int(current_node))
			current_node = shortest_copy.index(min(shortest_copy))

			# Find the node with the shortest distance as the next current node
			# and meanwhile this node should have not been visited yet
			# We replace the distance in the unsatisfied current node with 999
			while current_node not in not_visited:
				shortest_copy[current_node] = 999
				current_node = shortest_copy.index(min(shortest_copy))
				# All nodes have been visited
				if shortest_copy == [999 for _ in range(250)]:
					print('shortest_path',shortest_path[target])
					print('distance', shortest_dist[target])
					return 

if __name__ == '__main__':
	f = open('edges.txt')
	lines = f.readlines()
	num_station = 250
	node_dist = {}
	for i in range(num_station):
		node_dist[str(i)] = {}

	for line in lines:
		start = line.split('\t')[0]
		end = line.split('\t')[1]
		dist = line.split('\t')[2].strip()
		node_dist[start][end] = int(dist)		# {'0':{'1':2,'2':3}, '1':{'2':3}, ...} 

	start_node = 1
	end_node = 198
	Dijkstra(node_dist, start_node, end_node)

	