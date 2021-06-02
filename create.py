import xml.etree.ElementTree as ET


f = open('qwert.xml','w')

root = ET.Element('data')

country = (ET.Element('jhj', user="u9", password="xthyjskm2000", host = '9', port = '4', database = '9'))


root.append(country)


# NOTE: По аналогии выше сами заполните нужные вам страны

xml_str = ET.tostring(root, encoding="utf-8", method="xml")
x= xml_str.decode(encoding="utf-8")
f.write(x)
f.close()