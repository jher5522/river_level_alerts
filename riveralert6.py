#This version aims to add links to appropriate weather reports. And the graph of the trend. 

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
#when there is only 1 email address it splits on teh letters instead of the word...


#rivers that we don't care about
badrivers = [
'Molonglo River at Burbong',
'Paddys River at Riverlea',
'Molonglo R at Coppins Crossing',
'Deua/Moruya River at Wamban',
'Queanbeyan River at Wickerslack',
'Clyde River at Brooman',
'Tuross River at D/S Wadbilliga Junct',
'Gudgenby River at Naas',
'Murray River at Biggara']


#create the message
message = ''
for i in range(len(riverLevels)):

    #assign the values in the array riverLevels[i]
    [river, level, req] = riverLevels[i]

    if not river in badrivers:
        #retrieve a string describing how likely it is that the river will be up on teh weekend
        liklihood = func.liklihood(level, req)
        excess = float(level) - float(req)
        links = func.links(river.strip())
        
        #if the current river is up, add its info to the message
        if excess >= 0:
            message = message + '\n\n' + river + liklihood + 'It is ' + str(excess) + 'm above the minimum level.\n[' + str(level) + 'm/' + str(req) + 'm]\n' + links
      
TO = ['herbertjemma@gmail.com', 'a.houghton@exemail.com.au']

print message

emailprac.sendmail(TO, message, "river alerts")


