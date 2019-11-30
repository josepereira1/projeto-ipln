#!/usr/bin/python3

import re
from lxml import etree	#	ferramenta

regIP = "\s[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
regURL = "https?://[A-Za-z0-9\.\/\-\_\#\?\=\&\%]+"


def parseXML(filename):
	tree = etree.parse(filename)	#retorna um ElementTree object e não um Element object
	root = tree.getroot()
	return root


def top_reg_in_files(filenames : list, attributes : list, regex : str, N : int):

	dic = {}
	
	for idx, filename in enumerate(filenames):
		root = parseXML(filename)
		for child in root.iter():
			text = str(child.get(attributes[idx])) 
			urls = re.findall(regex, text) # applies regex to string
			for url in urls:
				if url not in dic: dic[url] = 1
				else: dic[url] += 1

	lst = sorted(dic.items(), key=lambda url: url[1], reverse=True)
	return lst[:N]


filenames = ["stackoverflow/big/Posts.xml", "stackoverflow/big/Users.xml","stackoverflow/big/Comments.xml"]
attributes = ["Body", "AboutMe", "Text"]

ips = top_reg_in_files(filenames, attributes, regIP, 3)
print(ips) 

urls = top_reg_in_files(filenames, attributes, regURL, 3)
print(urls) 

