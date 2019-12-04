#!/usr/bin/python3

import re
from lxml import etree	#	ferramenta
import sys
from getopt import getopt



regIP = r"[ \,\;\:]([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})[ \,\.\;\:\!\?]"
regURL = r"https?://[A-Za-z0-9\.\/\-\_\#\?\=\&\%]+"
regLang = r"(java|python|haskell|C#|mysql|mongodb)"

output_dir = "output/"


def from_xml(filename):
	tree = etree.parse(filename)	#retorna um ElementTree object e não um Element object
	root = tree.getroot()
	return root


#	converte o dicionário em formato ElementTree e guarda num ficheiro
#	dict: dicionário a escrever
#	agregation: a categoria, p.e. posts, comments, users
# 	single: elemento da agregação, sendo respetivamente post, comment, user
def to_xml(lst : list):
	root = etree.Element("elements")
	iteration = 0;

	for key, val in lst: 
		root.append(etree.Element("element"))
		root[iteration].set("key", str(key))
		root[iteration].set("value", str(val))
		iteration = iteration + 1

	f = open(output_dir + "elements.xml","w")
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


# ex: permite para o atributo especificado armazenar o respetivo valor caso o mesmo tenha correspondência com a regex.
# output: a regex regIP mostra que os 3 posts com mais score: Id="91782" => 56
#                                                             Id="164489" => 50
#                                                             Id="76535" => 45
def top_reg_sort_by_atribute(filenames : list, attributes : list, regex : str, N : int, keyAttr : int, castInt: bool):

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
					if idElem not in dic: 
						if castInt: dic[idElem] = int(text)
						else: dic[idElem] = text

	lst = sorted(dic.items(), key=lambda reg: reg[1], reverse=True)
	return lst[:N]


def pretty_print(data: list, left_text: str, right_text: str):
	num_palavras_coluna_esquerda = len(left_text)	
	num_palavras_coluna_direita = len(right_text)

	limits = "|-" + spaces(len(left_text) + 3 + len(right_text), "-") + "-|"

	print(limits)
	print("| " + left_text + " | " + right_text + " |")
	for elem in data:
		print("| " + str(elem[0]) + spaces(num_palavras_coluna_esquerda - len(str(elem[0])) +1, " ") + "| " + str(elem[1]) + spaces(num_palavras_coluna_direita - len(str(elem[1])), " ") + " |")
	print(limits)

def spaces(num: int, ch):
	tmp = ""
	for i in range(0,num):
		tmp += ch

	return tmp

#	python3 xmlstats.py -t '1' -f 'data/Comments.xml' -a 'Text' -r 'java' -l 100
def main():
	opts, resto = getopt(sys.argv[1:],"help:h:t:f:a:r:c:l")

	if opts[0][0] == "-h":	#	HELP
		print("[top_reg_by_elem] -t <<type == 0>> -f <<files>> -a <<attributes>> -r <<regex>> -l <<limit>>")
		print("[top_reg_by_file] -t <<type == 1>> -f <<files>> -a <<attributes>> -r <<regex>> -l <<limit>>")
		print("[top_reg_sort_by_atribute] -t <<type == 2>> -f <<files>> -a <<attributes>> -r <<regex>> -c <<cast int (1 = yes & 0 = no), if attribute is integer>> -l <<limit>>")
		sys.exit(1)
	
	tipo = opts[0][1]
	filenames = opts[1][1].split(',')
	attributes = opts[2][1].split(',')
	regex = opts[3][1]
	limit = int(resto[0])

	if tipo == "0":
		res = top_reg_by_elem(filenames, attributes, regex, limit, "Id")
		pretty_print(res, "Id da entidade", "Número de ocorrências da regex")
		to_xml(res)
	elif tipo == "1":
		res = top_reg_in_file(filenames, attributes, regex, limit)
		pretty_print(res, "Expressão regular", "Número de ocorrências da regex")
		to_xml(res)
	elif tipo == "2":
		castInt = opts[4][1]
		if(castInt == "0"): 
			castInt = False
		elif castInt == "1": 
			castInt = True
		else:
			print("Error on argument <<c>>!")
			sys.exit(1)
		res = top_reg_sort_by_atribute(filenames, attributes, regex, limit, "Id", bool(castInt))
		pretty_print(res, "Id da entidade", "Valor do atributo")
		to_xml(res)
	else:
		print("Error on type!")

main()

	

