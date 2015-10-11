__author__ = 'saipc'

#7AXR-R7I5-178D-4333:footastic
#https://supportmyclub.wufoo.com/api/v3/forms/x7o68ah12q3jf2/entries.json?pretty=true
#https://supportmyclub.wufoo.com/api/v3/forms/x7o68ah12q3jf2/entries.json?pretty=true --> Works!!!
import requests
def curl(noOfRequests):
    for x in xrange(0, noOfRequests):
        r = requests.get('https://supportmyclub.wufoo.com/api/v3/forms/x7o68ah12q3jf2/entries.json?pretty=true&pageStart='+str(100 * x)+'&pageSize=100', auth=('7AXR-R7I5-178D-4333', 'footastic'))
        with open('sample'+str(x + 1)+'.txt','w') as file:
            #print r.text
            file.write(r.text)

curl(5)
