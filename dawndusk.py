#Prints the time for the next dawn & dusk

import datetime
from astral import Astral

a = Astral()
location = a.geocoder
loc = location["Dallas"]

now = datetime.datetime.today()

#Sun's location for current date
sun = loc.sun(date=datetime.date(now.year, now.month, now.day), local=True)
#Sun's location for tomorrow
suntomorrow =  loc.sun(date=now + datetime.timedelta(days=1),local=True) 

print "time is: ", now.strftime("%H:%M")

if now.hour < sun["dawn"].hour:
	print "Dawn is at ", sun["dawn"].strftime("%H:%MPM %m/%d/%y")
	print "Dusk is at: ", sun["dusk"].strftime("%H:%MAM %m/%d/%y")
if now.hour > sun["dawn"].hour and now.hour < sun["dusk"].hour:
	print "Tomorrow's dawn is at:", suntomorrow["dawn"].strftime("%H:%MAM %m/%d/%y") 
	print "Dusk is at: ", sun["dusk"].strftime("%H:%MPM %m/%d/%y")
else:
	print "Tomorrow's dawn is at: ", suntomorrow["dawn"].strftime("%H:%MAM %m/%d/%y")
	print "Tomorrow's dusk is at: ", suntomorrow["dusk"].strftime("%H:%MPM %m/%d/%y")