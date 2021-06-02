import xml.etree.ElementTree as ETree

parser = ETree.XMLParser(encoding="utf-8")
tree = ETree.parse("appt.xml", parser=parser)
root = tree.getroot()
print(ETree.tostring(tree.getroot()))

# for child in root:
#      print(child.tag, child.attrib)



for child in root.findall('begin'):
    h_value = child.get('begin/tupe')
    t_value = child.get('password')
    print(t_value, h_value)
