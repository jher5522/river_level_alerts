def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def riverDrop(riverName,currentLevel,timeFromNow):
    #recognise the river and open the file witht he river data
    #look up the rivers data
    #Find the closest height to the current height
    #Look up the corresponding time to minimumlevel
    #return this time
    print ''


def liklihood(level,req):
    portionOver = float(level) /float(req)
    if portionOver < 1.5:
        liklihood = "might be up.\n"
    elif portionOver < 2:
        liklihood = "is up!\n"
    else:
        liklihood = "is WAY UP!\n"
    return liklihood


def links(river):
    import re
    import urllib2
    dict = {'Clyde River at Brooman' : ['http://www.kayakcanberra.com/rivers/clyde.gif', 'http://www.bom.gov.au/nsw/forecasts/ulladulla.shtml'],
             'Cotter River at Kiosk' : ['http://www.kayakcanberra.com//rivers/cotter.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml'], 
             'Deua/Moruya River at Wamban' : ['http://www.kayakcanberra.com//rivers/deua.gif','http://www.bom.gov.au/nsw/forecasts/batemansbay.shtml'] ,
             'Goobarragandra River at Lacmalac' : ['http://www.kayakcanberra.com//rivers/goobarragandra.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml'] ,
             'Goodradigbee River at Wee Jasper'  :['http://www.kayakcanberra.com//rivers/goodradigbee.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml'],
             'Gudgenby River at Naas'  :['http://www.kayakcanberra.com//rivers/gudgenby.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml'],
             'Gwydir R D/S Copeton Dam'  :['http://www.kayakcanberra.com//rivers/gwydir.gif','http://www.bom.gov.au/nsw/forecasts/tamworth.shtml'],
             'Kangaroo River at Hampden Bridge' :['http://www.kayakcanberra.com//rivers/kangaroo.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml']  ,
             'Molonglo River at Burbong'  : ['http://www.kayakcanberra.com//rivers/uppermolonglo.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml'],
             'Molonglo R at Coppins Crossing'  : ['http://www.kayakcanberra.com//rivers/molonglo.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml'],
             'Murray River at Biggara'  : ['http://www.kayakcanberra.com//rivers/murraygates.gif','http://www.bom.gov.au/nsw/forecasts/jindabyne.shtml'],
             'Murrumbidgee River at Lobbs Hole' : ['http://www.kayakcanberra.com//rivers/murrumbidgeeupper.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml']  ,
             'Murrumbidgee River at Mt Macdonald' : ['http://www.kayakcanberra.com//rivers/murrumbidgeelower.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml'],
             'Murrumbidgee River at Glendale (Childowlah)' :['http://www.kayakcanberra.com//rivers/childowlah.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml']  ,
             'Nymboida River at Nymboida'  : ['http://www.kayakcanberra.com//rivers/nymboida.gif','http://www.bom.gov.au/nsw/forecasts/grafton.shtml'],
             'Paddys River at Riverlea'  : ['http://www.kayakcanberra.com//rivers/paddys.gif','http://www.bom.gov.au/nsw/forecasts/mudgee.shtml'],
             'Queanbeyan River at Wickerslack' : ['http://www.kayakcanberra.com//rivers/queanbeyan.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml']  ,
             'Shoalhaven River at Hillview'  : ['http://www.kayakcanberra.com//rivers/shoalhaven.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml'],
             'Shoalhaven River at Grassy Gully'  : ['http://www.kayakcanberra.com//rivers/shoalhavenlower.gif','http://www.bom.gov.au/act/forecasts/canberra.shtml'],
             'Snowy River at McKillops Bridge'  : ['http://www.kayakcanberra.com//rivers/snowy.gif','http://www.bom.gov.au/nsw/forecasts/jindabyne.shtml'],
             'Tuross River at D/S Wadbilliga Junct'  : ['http://www.kayakcanberra.com//rivers/tuross.gif','http://www.bom.gov.au/nsw/forecasts/narooma.shtml'],
             'Wingecarribee River at Greenstead'  :['http://www.kayakcanberra.com//rivers/wingecarribee.gif','http://www.bom.gov.au/nsw/forecasts/wollongong.shtml'],
             'Wollondilly River at Golden Valley' :['http://www.kayakcanberra.com//rivers/wollondilly.gif','http://www.bom.gov.au/nsw/forecasts/wollongong.shtml']}

    #go to the weather html of the river and print its rain forecast in mm for the next 3 days
    #get the html of the kayak page
    response = urllib2.urlopen(dict[river][1])
    html = response.read()

    #remove all the formatting shit
    html = re.sub('\s+', ' ', html)
    weather = re.findall('<dd class="summary"[^<]*',html)
    forecast = 'weather tomorrow is: '+ weather[0][20:] + '\nSaturday: ' + weather[1][20:] + '\nSunday: ' + weather[2][20:]
    
    return forecast + '\nsee a plot of the levels at: ' + dict[river][0] + '\nsee the local weather at: ' + dict[river.strip()][1]


def format_email(text, image):
    # Send an HTML email with an embedded image and a plain text message for
    # email clients that don't want to display the HTML.

    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.MIMEImage import MIMEImage

    # Define these once; use them twice!
    strFrom = 'herbertjemma@gmail.com'
    strTo = strFrom

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'test message'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

   # We reference the image in the IMG SRC attribute by the ID we give it below
    msgMid = ''
#### NEED TO GET IMAGE ASWELL FROM LINKS FUNC
    for river in email_content.keys():
#####            image = '<img url=' + email_content[river][1]+'>'
            msgMid = '<tr> <td> ' + email_content[river][0] + '</td><td>' + image 

    msgStart = '<b>Some <i>HTML</i> text</b> and an image.<br> <table>'
    msgEnd = "</table>  <br>Nifty!"
    msgText = MIMEText( msgStart + msgMid + msgEnd, 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open('test.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)
