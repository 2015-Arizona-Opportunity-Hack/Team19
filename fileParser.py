__author__ = 'saipc'
from bs4 import BeautifulSoup
import json
import re
with open('sample.txt','r') as file:
    # print file.read()
    soup = BeautifulSoup(file.read(), 'html.parser')
    reg = re.compile(r'OUTPUT = ({.*};)', re.DOTALL)
    m = re.search(reg, soup.find_all('script')[1].get_text())
    print m.group(1)
    with open('decodedJson.txt', 'w') as writer:
        writer.write(m.group(1))
    jsonData = json.loads(m.group(1))
    print jsonData
