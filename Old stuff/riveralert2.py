import re
import urllib2

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
html = re.sub('<[^>]*>', '', html)

#cut it down to only the table content
html = html.split()
tablecontent = html[40:-171]


#run through the table contents.
#if you come across something which only contains numbers and decimal points its a river lever
#compare this number with the next number
#if the first is greater than the second add it to a list of rivers that are up
for word in tablecontent:
    if is_number(word):
        print word



