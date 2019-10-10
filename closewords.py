#!/usr/bin/env python3

import re
import sys

filename = sys.argv[1]
word = sys.argv[2]
number = str(int(sys.argv[3])-1) # our algorithm iterates till last word

text = open(filename).read() # reads all file to string
regex = "(" + word + "(?:[\ \t\n\,\;\:\"\'\[\]\(\)]+\w+(?:(?:[\-\@\.\w]*)\w+)?){1," + number + "})"
lines = re.findall(regex, text) # applies regex to string

dic = {} # init dic

for line in lines:
	
	# remove 'trash' from string
	clean = re.sub('[\n\,\;\:\"\'\[\]\(\)]+', '', line).replace('\t',' ')
	# splits by space
	words = clean.split(' ')
	# first word is never used, ex: 'está'
	words.pop(0)
	
	key = ""
	i = 0
	for word in words:
		
		# increment key:
		# words = ['um', 'lindo', 'dia'] 
		# ex: key = um
		#     key = um lindo 
		#     key = um lindo dia
		if key == "": key = words[i]
		else: key = key + " " + words[i]
		i = i + 1 
		
		# increment number of hits
		if key in dic: dic[key] = dic[key] + 1	
		else: dic[key] = 1	


# sort alphabetically Hash Table by key
for key in sorted(dic.keys()):
	if key.find(" ") == -1:print("---------------")
	print(key, "(" + str(dic[key]) + ")")

print("---------------")