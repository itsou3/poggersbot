#Prints the time for the next dawn & dusk

import datetime
import pytz
from astral import Astral

a = Astral()
location = a.geocoder
loc = location["Dallas"]
now = pytz.timezone("US/Central").localize(datetime.datetime.now())

#Sun's location for current date
sun = loc.sun(date=datetime.date(now.year, now.month, now.day), local=True)
#Sun's location for tomorrow
suntomorrow =  loc.sun(date=now + datetime.timedelta(days=1),local=True) 

print "Current Time: ", now.strftime("%H:%M")

while True:
	if now < sun["dusk"]:
		dawnt = sun["dawn"].strftime("%H:%MAM %m/%d/%y")
		duskt = sun["dusk"].strftime("%H:%MPM %m/%d/%y")		
		if now > sun["dawn"]:
			dawnt = suntomorrow["dawn"].strftime("%H:%MAM %m/%d/%y")
	else:
		dawnt = suntomorrow["dawn"].strftime("%H:%MAM %m/%d/%y")
		duskt = suntomorrow["dusk"].strftime("%H:%MAM %m/%d/%y")
	print "Next dawn: ", dawnt 
	print "Next dusk: ", duskt
	break


