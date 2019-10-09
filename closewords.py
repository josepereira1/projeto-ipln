#!/usr/bin/env python3

import re
import sys

filename = sys.argv[1]
word = sys.argv[2]
number = sys.argv[3]

text = open(filename).read()

#regex = "("+word+"(?:[\ \t\n\,\;\:\"\'\[\]\(\)\&]+\w+(?:(?:\-|[\@\.\w]*)\w+)?){1,"+number+"})"

output = re.findall(regex, text)

print(output)

#cona = ""

# for elem in output:
#  	for ch in elem:
#  		if ch != ' ':
#  			cona = cona + ch


# print(cona)



