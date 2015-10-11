#!/usr/bin/python2.7

print "Content-type: text/html"
print

import json
import psycopg2
from ibf2 import *
from recoEmailHelpers import *
# using ibf2 instead of ibf, can interchange with ibf
# to generate reverse combinations
if __name__ == "__main__":
    try:
        jsonData = json.loads(getJson('Volleyball Shoes'))
        name = jsonData[1][0]
        name = name[1]
        listRecoScores = jsonData[0]
        listReco = listRecoScores
        #print name, listReco
        #name = "Sai Pc"
        email = generateRecoEmail(name, listReco)
        # print email
        if name is not None:
            conn = psycopg2.connect(database="SMC", user="postgres", password="dragon123", host="127.0.0.1", port="5432")
            cur = conn.cursor()
            query = 'select "Email" from "Orders" WHERE "CustomerName" = \'%s\''
            #print query%(name)
            cur.execute(query%name)
            row = cur.fetchone()
            them = row[0]
            them = "schand31@asu.edu"
            sendEmail(email, them, 'New Requests of Interest to YOU!')
            print "Recommendations Email successfully sent to ", them
            print email
    except Exception as e:
        print e
