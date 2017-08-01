class School(object):
	def __init__(self, name):
		self.name = name
		self.roster = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
		
	def addStudent(self, name, grade):
		self.roster[grade].append(name)
		print "Added %s to %s grade roster" % (name, grade)
		
	def printRoster(self, grade):
		#print self.roster[grade]
		print '\n'.join(self.roster[grade])
		
	def __str__(self):
		all_sorted = ""
		for g in self.roster.keys():
			all_sorted += "Grade %s has children %s \n" %(g, sorted(self.roster[g]))
		return all_sorted
		
	def __repr__(self):
		return self.__str__()
	

johnson = School("Johnson")
johnson.addStudent("Erin", 2)
johnson.addStudent("Bob", 2)
johnson.printRoster(2)
print "__str__"
print johnson
print "__repr__"
johnson