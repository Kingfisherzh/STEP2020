def rec(prev_candidate, char_index, random_word, sorted_dictionary):
	if char_index >= random_word.size()
	return ""
	anagram_candidate = binarySearch(prev_candidate, sorted_dictionary)
	if anagram_candidate:
		return anagram_candidate

	anagram_candidate_with_char = rec(prev_candidate+random_word[char_index],char_index+1,random_word,sorted_dictionary)
	if anagram_candidate_with_char:
		return anagram_candidate_with_char

	anagram_candidate_without_char = rec(prev_candidate,char_index+1,random_word,sorted_dictionary)
	if anagram_candidate_without_char:
		return anagram_candidate_without_char

def recursive_solution(random_word, sorted_dictionary):
	rec('',0,random_word,sorted_dictionary)
def binarySearch(random_word, sorted_dictionary):
				