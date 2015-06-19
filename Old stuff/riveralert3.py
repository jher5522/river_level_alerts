#this one will try and get more details on what is in the table, rather than just trim the list

import re
import urllib2
import emailprac


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


#get the html of the kayak page
response = urllib2.urlopen('http://www.kayakcanberra.com/heights/')
html = response.read()

#remove all the formatting shit
html = re.sub('\s+', ' ', html)
html = re.sub('<td>', '*** ', html)
html = re.sub('<[^>]*>', '', html)
html = html.split('***')

message = ''

#run through each cell in the table. Print out the river levels.
#there are 5 columns, i want column 2,3
for i in range(len(html)):
        if (i-2)%5 == 0 and is_number(html[i]):
                Height = html[i]
                Level = html[i+1]
                if Height > Level:
                    Excess = float(html[i]) - float(html[i+1])
                    message = message + '\n' + html[i-1] + 'is up! It is ' + str(Excess) + 'm above the minimum level'
        

TO = "herbertjemma@gmail.com"

print message

emailprac.sendmail("herbertjemma@gmail.com", message, "river alerts")


