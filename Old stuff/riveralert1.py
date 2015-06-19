import re
import urllib2
response = urllib2.urlopen('http://www.kayakcanberra.com/heights/')
html = response.read()

html = re.sub('\s+', ' ', html)
html = re.sub('<[^>]*>', '', html)

html = html.split()
tablecontent = html[40:-171]

print tablecontent
