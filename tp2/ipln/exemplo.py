#!/usr/bin/python3

#	COMO INSTALAR: python3 -m pip install lxml

from lxml import etree	#	ferramenta

root = etree.parse("Posts.xml")

# for elem in root.iter():
# 	idElem = str(elem.get("Id"))
# 	score = str(elem.get("Score"))
# 	print(idElem + " | " +  score)

# ------------------------------------

# root = etree.Element("html")

# # print(root.tag)

# root.append(etree.Element("head"))

# root[0].append(etree.Element("title"))
# root[0][0].text = "Title"

# root.append(etree.Element("body"))

# root[1].append(etree.Element("a"))
# root[1][0].text = "link"

# root[1][0].set("href", "https://github.com/andrefs/ipln-1920-i")
# root[1][0].set("class", "classx")


print(etree.tostring(root, pretty_print = True, encoding='unicode'))