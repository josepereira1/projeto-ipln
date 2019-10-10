#!/usr/bin/env python3

import re
import sys

def capture(filename, mode, number, word):
	text = open(filename).read() # reads all file to string
	if mode == "-A": regex = "(" + word + "(?:[\ \t\n\,\;\:\"\'\[\]\(\)]+\w+(?:(?:[\-\@\.\w]*)\w+)?){1," + number + "})"
	else: regex = "(?:(?:(?:(?:\w+[\-\@\.\w\:\/]*)?)\w+[\ \t\n\,\;\:\"\'\[\]\(\)]*\ ){1," + number +"}"+ word +")"

	return re.findall(regex, text) # applies regex to string

def store(lines):
	dic = {} # init dic

	for line in lines:
		
		# remove 'trash' from string
		clean = re.sub('[\,\;\:\"\'\[\]\(\)]+', '', line).replace('\t',' ')
		clean = re.sub('\n', ' ', clean)
		# splits by space
		words = clean.split(' ')
		# first word is never used, ex: 'está'
		if mode == "-A": words.pop(0)
		else: del(words[len(words)-1])
		
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

	return dic

def displayMatrix(keys, dic):
	N = 50

	mat = [ [ 0 for l in range(N) ] for c in range(N) ]
	c = -1
	l = 0

	maxspaces = 0

	for key in keys:
		if ' ' not in key: # col change
			l = 0
			c = c + 1
		else:
			l = l + 1
		mat[l][c] = key
		n = len(key) + len(str(dic[key]))
		if n > maxspaces:
			maxspaces = n

	maxl = l + 1
	maxc = c + 1
	maxn = max(dic.values())

	# at this moment maxword and it's length is already known

	for l in range(0, maxl):
		for c in range(0, maxc):
			key = mat[l][c]
			if key != 0:
				print(key, end='') # PRINTAR A KEY
				for i in range(0, maxspaces - len(key) - len(str(dic[key]))): # PRINTAR OS ESPAÇOS
					print(' ', end='')
				print(' (' + str(dic[key]) + ') | ', end='') # PRINTAR O NÚMERO E SEPARAÇÃO
			else:
				for i in range(0, maxspaces + 3): # PRINTAR OS ESPAÇOS
					print(' ', end='') 
				print(' | ', end='') # PRINTAR SEPARAÇÃO
		print(' ')

# ---------------------------------------------------------------

mode = sys.argv[1]
word = sys.argv[2]
filename = sys.argv[3]
number = str(int(sys.argv[4])-1) # our algorithm iterates till last word

lines = capture(filename, mode, number, word)

if not lines: 
	print("Do not exist word " + word)
	sys.exit()

dic = store(lines)

keys = list(sorted(dic.keys()))

displayMatrix(keys, dic)


