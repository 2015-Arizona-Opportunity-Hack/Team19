__author__ = 'saipc'
import psycopg2
conn = psycopg2.connect(database="SMC", user="postgres", password="dragon123", host="127.0.0.1", port="5432")
cur = conn.cursor()
table_name1 = "Orders"
table_name2 = "productData"
table_name3 = "wufooforms"
query = 'select * from "Orders", "productData", "wufooforms" where "Orders"."ProductName" = "productData"."ProductName" and "wufooforms"."orderID" = "Orders"."OrderID" '
print query
cur.execute(query)
rows = cur.fetchall()
count = 0
for row in rows:
    #print row
    count += 1
print count
conn.commit()

# select * from "Orders", "productData" where "Orders"."ProductName" = "productData"."ProductName"
