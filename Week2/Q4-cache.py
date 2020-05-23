import sys

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
class Cache:
	# Initializes the cache.
	# |n|: The size of the cache.
	def __init__(self, n):
		self.length = n
		self.dic = {}


	# Access a page and update the cache so that it stores the most
	# recently accessed N pages. This needs to be done with mostly O(1).
	# |url|: The accessed URL
	# |contents|: The contents of the URL
	def access_page(self, url, contents):
		# if contents exist, remove this key-value pair
		exist = self.dic.pop(contents, False)
		# if over long and contents don't exist, pop the first pair
		if not exist and len(self.dic) == self.length:
			first = list(self.dic.keys())[0]
			self.dic.pop(first)

		self.dic[contents] = url
		pass

	# Return the URLs stored in the cache. The URLs are ordered
	# in the order in which the URLs are mostly recently accessed.
	def get_pages(self):
		# return a list of keys in the reverse order
		pages = []
		values = list(self.dic.values())
		if self.dic:
			for i in range(len(self.dic)-1, -1,-1):
				pages.append(values[i])
			return pages
		else:
			return []	
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