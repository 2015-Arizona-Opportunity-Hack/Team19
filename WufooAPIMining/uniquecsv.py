__author__ = 'saipc'

with open('orders_export.csv', 'r') as csv:
    orderIDs = set()
    for line in csv:
        strings = line.split(",")
        if(len(strings) > 2):
            orderID = strings[0]
            email = strings[1]
            name = strings[24]
            donation = strings[11]
            productName = strings[17]

        nonNames = ['pending', 'true', 'fulfilled']
        if(orderID and email and name and name not in nonNames and donation):
            if orderID not in orderIDs:
                orderIDs.add(orderID)
                print (orderID + ',' + email + ',' + name)
                with open('orders', 'a') as writer:
                    writer.write(orderID + ',' + email + ',' + name + "," + productName +"\n")
                with open('recommenderData.csv', 'a') as writer:
                    writer.write(name + "," + productName + "," + donation +"\n")

            #orders[orderID] = (email, name)
