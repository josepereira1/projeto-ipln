#!/usr/bin/env python3

import re
import sys

text = open("input.txt").read()

#output = re.findall(r'(was(?:[\ \t\n\,\;\:\"\'\[\]\(\)\&]+\w+(?:(?:\-|[\@\.\w]*)\w+)?){1,5})', text)

output = re.findall(r'(was(?:[\ \t\n\,\;\:\"\'\[\]\(\)\&]+\w+(?:(?:\-|[\@\.\w]*)\w+)?){1,5})', text)


print(output)

