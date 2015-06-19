#This version aims to generate a 'maybe' if the river is only just above minimum and link you to the local weather.
#Maybe < 1.1*min, 1.1 < UP < 2, WAAAY UP > 2. It'll refer to the 'func' file instead of putting it all in here
#add a more consise restructuring of the centre of the program

#import all the modules and functions it'll need
import re
import urllib2
import emailprac
import func


#get the html of the kayak page
response = urllib2.urlopen('http://www.kayakcanberra.com/heights/')
html = response.read()

#remove all the formatting shit
html = re.sub('\s+', ' ', html)
html = re.sub('<td>', '*** ', html)
html = re.sub('<[^>]*>', '', html)
html = html.split('***')

#get the river name, level and required height for each river.
riverLevels = [[html[i-1],html[i], html[i+1]] for i in range(len(html)) if (i-2)%5 == 0 and func.is_number(html[i])]
#riverLevels = [name of river, level, required]. Might need to check these positions

#create the message
message = ''
for i in range(len(riverLevels)):
    #assign the values in the array riverLevels[i]
    [river, level, req] = riverLevels[i]
    #retrieve a string describing how likely it is that the river will be up on teh weekend
    liklihood = func.liklihood(level, req)
    excess = float(level) - float(req)
    #if the current river is up, add its info to the message
    if excess >= 0:
        message = message + '\n\n' + river + liklihood + ' It is ' + str(excess) + 'm above the minimum level.\n [' + str(level) + 'm/' + str(req) + 'm]\n'
  

TO = "herbertjemma@gmail.com, a.houghton@exemail.com.au"

print message

emailprac.sendmail(TO, message, "river alerts")


