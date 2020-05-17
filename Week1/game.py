# -*- coding: UTF-8 -*-
import sys
import urllib
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def HighScoreSolution(soup,dic):
	
	values = soup.find_all('div')

	alphabets = []
	for value in values:
		if value.string:
			alphabets.append(value.string.lower())
	# print(alphabets, len(alphabets))

	candidates = [""]
	anagrams = []
	highestScore = 0
	solution = ''
	len_dic = len(dic)
	for alp in alphabets:
		#print('candidates: ', candidates)
		words = candidates.copy()
		#print(words)
		for prev in words:
			word = prev + alp
			word = wordSort(word)
			anagram = binarySearch(word, dic, 1, len_dic-1)
			score = getScore(anagram)
			if anagram and highestScore < score:
				solution = [anagram, score]
				anagrams.append([anagram, getScore(anagram)])
				highestScore = score

			candidates.append(word)
	#print(anagrams)		
	#print(solution)
	if solution:
		return solution[0][1]
	else:
		return None

def wordSort(word):
	letters = sorted(word)
	word = ''
	for l in letters:
		word = word + l
	return word
		
def Submit(driver,dic):
	for i in range(10):
		soup = BeautifulSoup(driver.page_source, features='html.parser')
		solution = HighScoreSolution(soup,dic)
		last = False
		if solution:
			alphabets = list(solution)
			for alp in alphabets:
				alp = alp.upper()
				if alp == 'Q': 
					alp = 'Qu'
					last = True
				elif alp == 'U' and last == True:
					last = False
					continue	
				driver.find_element_by_xpath("//div[contains(text(),'" + alp + "')]").click()
			driver.find_element_by_xpath("//input[@value = 'Submit']").click()
		else:
			driver.find_element_by_xpath("//input[@value = 'PASS']").click()
	driver.find_element_by_xpath('//input[@placeholder = "皆に見せたい宛名"]').send_keys('Toki')
	driver.find_element_by_xpath('//input[@id="AgentRobot"]').click()
	driver.find_element_by_xpath('//input[@name="Name"]').send_keys('Yanjun Zhou')
	driver.find_element_by_xpath('//input[@name="Email"]').send_keys('kingfisherzh@gmail.com')
	
	#driver.find_element_by_xpath("//input[@value = 'Record!']").click()


def getScore(word):
	if word:
		alphabets = list(word[0])
		score = 0
		for alp in alphabets:
			if alp in ['j','k','x','z']:
				score += 3
			elif alp in ['c','f','h','l','m','p','v','w','y','q']:
				score += 2
			elif alp in ['a','b','d','e','g','i','n','o','r','s','t','u']:
				score += 1
		if score != 0:		
			return pow(score+1, 2)
		else:
			return 0	
	else:
		return 0

def binarySearch(word, new_dic, l, r):
	word_len = len(word)
	#print(word)
	#print(l,r)
	if l <= r:
		mid = int((l+r+1)/2)
		#print(word,l,r)
		#print(new_dic[mid])
		if new_dic[mid][0] == word:
			return new_dic[mid]
		elif new_dic[mid][0] > word:
			return binarySearch(word, new_dic, l, mid-1)		
		elif new_dic[mid][0] < word:
			return binarySearch(word, new_dic, mid+1, r)
	else:
		return None

def sortDictionary():
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
	return new_dic


	
if __name__ == '__main__':
	url = 'https://icanhazwordz.appspot.com/'
	driver = webdriver.Chrome()
	driver.get(url)
	dic = sortDictionary()

	Submit(driver,dic)
	#driver.find_element_by_xpath("//a[contains(text(),'Start a new game')]").click()

		