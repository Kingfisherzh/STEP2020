def Anagram(word):
	sorted_word = sorted(word)
	sorted_random_word = ''
	for c in sorted_word:
		sorted_random_word = sorted_random_word + c
	#print('sorted: ', sorted_random_word)
	f = open('./Dictionary.txt')
	lines = f.readlines()
	dic = []
	for line in lines:
		line = (line.strip()).lower()
		sorted_line = sorted(line)
		word = ''
		for c in sorted_line:
			word = word + c	
		dic.append([word,line])
	new_dic = sorted(dic, key=lambda x:x[0])

	dic_len = len(new_dic)
	anagram = binarySearch(sorted_random_word, new_dic, 0, dic_len)
	if anagram: 
		return anagram[1] 
	else: 
		return 'None'

def binarySearch(word, new_dic, l, r):
	word_len = len(word)
	if r >= 1 and l <= r:
		mid = int((l+r)/2)
		#print(new_dic[mid][0],  l, r)
		if new_dic[mid][0] == word:
			return new_dic[mid]
		elif new_dic[mid][0] > word:
			return binarySearch(word, new_dic, l, mid-1)		
		elif new_dic[mid][0] < word:
			return binarySearch(word, new_dic, mid+1, r)
	else:
		return None	


if __name__ == '__main__':
	word = 'debe'
	print('Anagram is', Anagram(word.lower()))