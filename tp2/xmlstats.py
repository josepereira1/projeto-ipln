#!/usr/bin/python3

import re
from lxml import etree	#	ferramenta
import sys
from getopt import getopt



regIP = r"[ \,\;\:]([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})[ \,\.\;\:\!\?]"
regURL = r"https?://[A-Za-z0-9\.\/\-\_\#\?\=\&\%]+"
regLang = r"(java|python|haskell|C#|mysql|mongodb)|[ \,\;\:]([CR])[ \,\.\;\:\!\?]"

output_dir = "output/"


def from_xml(filename):
	tree = etree.parse(filename)	#retorna um ElementTree object e não um Element object
	root = tree.getroot()
	return root


#	converte o dicionário em formato ElementTree e guarda num ficheiro
#	dict: dicionário a escrever
#	agregation: a categoria, p.e. posts, comments, users
# 	single: elemento da agregação, sendo respetivamente post, comment, user
def to_xml(lst : list, agregation : str, single : str):
	root = etree.Element(agregation)
	iteration = 0;

	for key, val in lst: 
		root.append(etree.Element(single))
		root[iteration].set("key", str(key))
		root[iteration].set("value", str(val))
		iteration = iteration + 1

	f = open(output_dir + agregation + ".xml","w")
	f.write(str(etree.tostring(root, pretty_print = True, encoding='unicode')))
	f.close()

	return root


# ex: permite calcular o número de ocorrências de palavras contidas numa regex em relação a um determinado elemento
# output: a regex regIP mostra que os 3 posts que publicaram mais IP's são: Id="91782" => 128 IP's
#                                                                           Id="164489" => 80 IP's
#                                                                           Id="76535" => 60 IP's

def top_reg_by_elem(filenames : list, attributes : list, regex : str, N : int, keyAttr : int):

	dic = {}

	for idx, filename in enumerate(filenames):
		root = from_xml(filename)
		for elem in root.iter():
			text = elem.get(attributes[idx])
			attr = elem.get(keyAttr); 
			if attr is not None:
				idElem = int(attr)
				regs = re.findall(regex, text)
				if len(regs) != 0:
					if idElem not in dic: dic[idElem] = len(regs)
					else: dic[idElem] += len(regs)

	lst = sorted(dic.items(), key=lambda reg: reg[1], reverse=True)
	return lst[:N]


# ex: permite calcular o número de ocurrências de palavras contidas numa regex em vários ficheiros
# output_2: a regex regIP mostra que os 3 IP's mais publicados são: '127.0.0.1' => 357 vezes
#                                                                   '0.0.0.0' => 152 vezes
#                                                                   '192.168.0.7' => 76 vezes

def top_reg_in_file(filenames : list, attributes : list, regex : str, N : int):

	dic = {}
	
	for idx, filename in enumerate(filenames):
		root = from_xml(filename)
		for child in root.iter():
			text = str(child.get(attributes[idx])) 
			regs = re.findall(regex, text) # applies regex to string
			for reg in regs:
				if reg not in dic: dic[reg] = 1
				else: dic[reg] += 1

	lst = sorted(dic.items(), key=lambda reg: reg[1], reverse=True)
	return lst[:N]

#	python3 xmlstats.py -t '1' -f 'data/Comments.xml' -a 'Text' -r 'java' -l 100
def main():
	opts, resto = getopt(sys.argv[1:],"help:h:t:f:a:r:l")

	if opts[0][0] == "-h":	#	HELP
		print("-t <<type>> -f <<files>> -a <<attributes>> -r <<regex>> -l <<limit>>")
		sys.exit(1)

	tipo = opts[0][1]
	filenames = opts[1][1].split(',')
	attributes = opts[2][1].split(',')
	regex = opts[3][1]
	limit = int(resto[0])

	if tipo == "0":
		res = top_reg_by_elem(filenames, attributes, regex, limit, "Id")
		print(res)
		to_xml(res, "elements", "element")
	elif tipo == "1":
		res = top_reg_in_file(filenames, attributes, regex, limit)
		print(res)
		to_xml(res, "elements", "element")
	else:
		print("Error on type!")

	# filenames = ["data/Posts.xml", "data/Users.xml", "data/Comments.xml"]
	# attributes = ["Body", "AboutMe", "Text"]

	# ips_mais_publicados = top_reg_in_file(filenames, attributes, regIP, 5)
	# print(ips_mais_publicados) 
	# to_xml(ips_mais_publicados, "ips_mais_publicados", "ip")

	# posts_com_mais_ips = top_reg_by_elem(["data/Posts.xml"], attributes, regIP, 3, "Id")
	# print(posts_com_mais_ips)
	# to_xml(posts_com_mais_ips, "posts_com_mais_ips", "ip")

main()

	

