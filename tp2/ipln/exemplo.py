#!/usr/bin/python3

#	COMO INSTALAR: python3 -m pip install lxml

from lxml import etree	#	ferramenta

# root = etree.parse("../data/Posts.xml")

# for elem in root.iter():
# 	idElem = str(elem.get("Id"))
# 	score = str(elem.get("Score"))
# 	print(idElem + " | " +  score)

# ------------------------------------

# root = etree.Element("html")
# print(root.tag)

# root.append( etree.Element("head") )
# head = etree.Element("head") 
# ------------------------------------------
# root.append(head)

# nota: root[0] <=> head 
# root[0].append( etree.Element("title") )
# root[0][0].text = "Title"
# ------------------------------------------
# title = etree.Element("title")
# title.text = "Title"
# head.append(title)

# root.append( etree.Element("body") )
# ------------------------------------------
# body = etree.Element("body")
# root.append(body)

# nota: root[1] <=> body
# root[1].append( etree.Element("link") )
# root[1][0].text = "link"
# ------------------------------------------
# link = etree.Element("a")
# link.text = "link"
# body.append(link)

# root[1][0].set("href", "https://github.com/andrefs/ipln-1920-i")
# root[1][0].set("class", "classx")
# link.set("href", "https://github.com/andrefs/ipln-1920-i")
# link.set("class", "classx")

# print(etree.tostring(root, pretty_print = True, encoding='unicode'))







