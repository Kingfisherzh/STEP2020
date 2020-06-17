from collections import defaultdict


def Dijkstra(node_dist, current_node, target):
	not_visited = [_ for _ in range(num_station)]
	shortest_dist = {}
	for i in range(num_station):
		shortest_dist[str(i)] = 999							# Initialize the distance
	shortest_path = [[] for _ in range(num_station)]		# Record paths
	shortest_dist[str(current_node)] = 0					# Distance from start node is 0
	
	while not_visited:
		if current_node in not_visited:
			if node_dist[str(current_node)]:
				for node in node_dist[str(current_node)].keys():
					if shortest_dist[str(node)] > shortest_dist[str(current_node)] + node_dist[str(current_node)][node]:
						shortest_dist[str(node)] = shortest_dist[str(current_node)] + node_dist[str(current_node)][node]
						for prev_node in shortest_path[int(current_node)]:
							shortest_path[int(node)].append(prev_node)
						shortest_path[int(node)].append(str(current_node))
						
			
			shortest_record = sorted(shortest_dist.items(), key=lambda shortest_dist:shortest_dist[1])
			not_visited.remove(int(current_node))
			current_node = shortest_record[0][0]
			count = 0
			# Find the node with the shortest distance as the next current node
			# and meanwhile this node should have not been visited yet
			
			while int(current_node) not in not_visited:
				if count == 249:
					print('shortest_path',shortest_path[target])
					print('distance', shortest_dist[str(target)])
					return
				else:	 
					count += 1
					current_node = int(shortest_record[count][0])
			
				

if __name__ == '__main__':
	f = open('edges.txt')
	lines = f.readlines()
	num_station = 250
	node_dist = {}
	for i in range(num_station):
		node_dist[str(i)] = defaultdict(dict)

	for line in lines:
		start = line.split('\t')[0]
		end = line.split('\t')[1]
		dist = line.split('\t')[2].strip()
		node_dist[start][end] = int(dist)		# {'0':{'1':2,'2':3}, '1':{'2':3}, ...} 

	start_node = 33
	end_node = 198
	Dijkstra(node_dist, start_node, end_node)

	



























