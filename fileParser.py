__author__ = 'saipc'
from bs4 import BeautifulSoup
import json
import psycopg2
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
        fields = ['Field1', 'Field2', 'Field11', 'Field13', 'Field15', 'Field21']
        for entry in Entries:
            count = 0
            for field in entry:
                if field in fields and entry[field]:
                    count += 1
                if count == 6 :
                    message, imageURL, schoolName, clubName, productName,orderID  = (entry[x] for x in fields)
                    #print field, entry[field]
                    print schoolName, clubName, productName,orderID, message
                    conn = psycopg2.connect(database="SMC", user="postgres", password="dragon123", host="127.0.0.1", port="5432")
                    cur = conn.cursor()
                    table_name = "wufooforms"
                    query = 'INSERT INTO "'+table_name+'" VALUES (%s, %s, %s, %s, %s, %s)'
                    email = "schand31@asu.edu"
                    name = "Sai Pc"
                    #print query%(orderID, email, name, productName)
                    cur.execute(query,(schoolName, clubName, productName,orderID, message, imageURL))
                    conn.commit()
        #with open('decodedJson.txt', 'a') as writer:
         #   writer.write(m.group(1))
