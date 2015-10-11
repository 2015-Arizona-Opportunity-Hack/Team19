__author__ = 'saipc'

with open('orders_export.csv', 'r') as csv:
    orderIDs = set()
    orders = dict()
    for line in csv:
        strings = line.split(",")
        if(len(strings) > 2):
            orderID = strings[0]
            email = strings[1]
            name = strings[24]

        nonNames = ['pending', 'true', 'fulfilled']
        if(orderID and email and name and name not in nonNames):
            print orderID, email, name
            #orders[orderID] = (email, name)

