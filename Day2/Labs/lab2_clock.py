class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):
    	return "The time is %s:%s" % (self.hour, self.minutes)
    
    def __add__(self, minutes):
      	total_minutes = self.minutes + minutes
      	if total_minutes < 60 and total_minutes > 0:
      		self.minutes = total_minutes
      	else:
      		self.minutes = total_minutes % 60
      		self.hour += round(total_minutes / 60)
      		
      	if self.hour > 24:
      		self.hour -= 24
      	
      	if self.hour <= 0:
      		self.hour = 24
    
    def __sub__(self, minutes):
    	minutes *= -1
      	self.__add__(minutes)
    	
     
    def __eq__(self, other):
    	return self.hour == other.hour and self.minutes == other.minutes
    	  
    def __ne__(self, other):  
    	return not self.__eq__



clock1 = Clock(12, 45)
clock2 = Clock(12, 45)

print clock1 == clock2
print clock1 != clock2

print "testing addition"
clock1 + 60
print clock1.minutes
print clock1.hour

print "testing subtraction"
clock2 - 5
print "minutes: %s" % clock2.minutes
print "hour: %s" %  clock2.hour

clock2 - 65
print "minutes: %s" % clock2.minutes
print "hour: %s" %  clock2.hour

clock3 = Clock(1, 5)
clock3 - 60
print "minutes: %s" % clock3.minutes
print "hour: %s" %  clock3.hour

