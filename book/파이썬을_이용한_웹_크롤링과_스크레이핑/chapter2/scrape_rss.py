from urllib.request import urlopen
from xml.etree import ElementTree

f = urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109')
tree = ElementTree.parse(f)

root = tree.getroot()

for item in root.findall('channel/item/description/body/location/data'):
    tm_ef = item.find('tmEf').text
    tmn = item.find('tmn').text
    tmx = item.find('tmx').text
    wf = item.find('wf').text
    print(tm_ef, tmn, tmx, wf)
