#This version aims to add links to appropriate weather reports. And the graph of the trend. 

#import all the modules and functions it'll need
import re
import urllib2


#get the html of the kayak page
response = urllib2.urlopen('http://www.kayakcanberra.com/heights/')
html = response.read()

#remove all the formatting shit
html = re.sub('\s+', ' ', html)
html = re.sub('<td>', '*** ', html)
links = re.findall("<a href[^>]*.gif'>",html)
links = re.findall("/.*gif",'\n'.join(links))
print 'http://www.kayakcanberra.com/'+'\nhttp://www.kayakcanberra.com/'.join(links)

