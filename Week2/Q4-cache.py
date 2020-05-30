import sys

class Node:
	def __init__(self, key=None, value=None):
		self.contents = key
		self.url = value
		self.prev = None
		self.next = None

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
class Cache:
	# Initializes the cache.
	# |n|: The size of the cache.
	def __init__(self, n):
		self.length = n
		self.head = Node()
		self.tail = Node()
		self.hashmap = {}	# hashmap = {[node.contents: node.url], ...}
		self.head.next = self.tail
		self.tail.prev = self.head


	# Access a page and update the cache so that it stores the most
	# recently accessed N pages. This needs to be done with mostly O(1).
	# |url|: The accessed URL
	# |contents|: The contents of the URL
	def access_page(self, url, contents):
		# Contents in keys
		if contents in self.hashmap.keys():
			node = self.hashmap[contents]
			Cache.move_out(self, node)
		# Contents not in keys
		else:
			if len(self.hashmap) == self.length:
				Cache.remove_first_node(self, self.head.next)
			# Create new node
			node = Node(contents, url)
			self.hashmap[contents] = node
		# Add the new node to before tail
		if len(self.hashmap) <= self.length:
			Cache.add_to_tail(self, node)	
		pass
	
	def remove_first_node(self, first):
		self.hashmap.pop(first.contents)
		# Build link between head and new 1st node
		self.head.next = first.next
		first.next.prev = self.head
		# Clear link from old 1st node
		first.next = None
		first.prev = None
		pass


	def move_out(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev
		pass


	def add_to_tail(self, node):
		# Link between last node and new node
		self.tail.prev.next = node
		node.prev = self.tail.prev
		# Link between new node and tail
		node.next = self.tail
		self.tail.prev = node
		pass



	# Return the URLs stored in the cache. The URLs are ordered
	# in the order in which the URLs are mostly recently accessed.
	def get_pages(self):
		pages = []
		node = self.tail
		while node.prev:
			if node.url:
				pages.append(node.url)
			node = node.prev
		return pages	
		pass


	# Does your code pass all test cases? :)
def cache_test():
	# Set the size of the cache to 4.
	cache = Cache(4)

	# Initially, no page is cached.
	equal(cache.get_pages(), [])
	# Access "a.com".
	cache.access_page("a.com", "AAA")
	# "a.com" is cached.
	equal(cache.get_pages(), ["a.com"])
	# Access "b.com".
	cache.access_page("b.com", "BBB")
	# The cache is updated to:
	#   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
	equal(cache.get_pages(), ["b.com", "a.com"])
	# Access "c.com".
	cache.access_page("c.com", "CCC")
	# The cache is updated to:
	#   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
	equal(cache.get_pages(), ["c.com", "b.com", "a.com"])
	# Access "d.com".
	cache.access_page("d.com", "DDD")
	# The cache is updated to:
	#   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
	equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
	# Access "d.com" again.
	cache.access_page("d.com", "DDD")
	# The cache is updated to:
	#   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
	equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
	# Access "a.com" again.
	cache.access_page("a.com", "AAA")
	# The cache is updated to:
	#   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
	equal(cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
	cache.access_page("c.com", "CCC")
	equal(cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
	cache.access_page("a.com", "AAA")
	equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
	cache.access_page("a.com", "AAA")
	equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
	# Access "e.com".
	cache.access_page("e.com", "EEE")
	# The cache is full, so we need to remove the least recently accessed page "b.com".
	# The cache is updated to:
	#   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
	equal(cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
	# Access "f.com".
	cache.access_page("f.com", "FFF")
	# The cache is full, so we need to remove the least recently accessed page "c.com".
	# The cache is updated to:
	#   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
	equal(cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
	print("OK!")
	pass

	# A helper function to check if the contents of the two lists is the same.
def equal(list1, list2):
	assert(list1 == list2)
	for i in range(len(list1)):
		assert(list1[i] == list2[i])
	pass
if __name__ == "__main__":
	cache_test()