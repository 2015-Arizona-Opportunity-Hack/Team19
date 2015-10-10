__author__ = 'saipc'

#7AXR-R7I5-178D-4333:footastic
#https://supportmyclub.wufoo.com/api/v3/forms/x7o68ah12q3jf2/entries.json?pretty=true
#https://supportmyclub.wufoo.com/api/v3/forms/x7o68ah12q3jf2/entries.json?pretty=true --> Works!!!
import requests
r = requests.get('https://supportmyclub.wufoo.com/api/v3/forms/x7o68ah12q3jf2/entries.json?pretty=true', auth=('7AXR-R7I5-178D-4333', 'footastic'))
with open('sample.txt','w') as file:
    #print r.text
    file.write(r.text)