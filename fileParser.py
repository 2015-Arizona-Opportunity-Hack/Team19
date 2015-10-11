__author__ = 'saipc'
from bs4 import BeautifulSoup
import json
import re
for x in xrange(0,5):
    with open('sample'+ str(x + 1) +'.txt','r') as file:
        # print file.read()
        soup = BeautifulSoup(file.read(), 'html.parser')
        # reg = re.compile(r'OUTPUT = ({.*});', re.DOTALL)
        # m = re.search(reg, soup.find_all('script')[1].get_text())
        # print m.group(1)
        scripttag = soup.find_all('script')[1]

        scriptline = next((line for line in scripttag.string.splitlines() if 'OUTPUT' in line))
        data = scriptline.split('=', 1)[1].strip(' ;')
        jsonData = json.loads(data)
        # print jsonData
        Entries = jsonData["Entries"]
        count = 0
        fields = ['Field1', 'Field11', 'Field13', 'Field15']
        for entry in Entries:
            for field in entry:
                if field in fields and entry[field]:
                    print field, entry[field]
            count += 1
        #with open('decodedJson.txt', 'a') as writer:
         #   writer.write(m.group(1))
