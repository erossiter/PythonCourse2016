import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()


# TODO: print lines that do not contain the
keyword = re.compile(r"the ")
for line in text:
	if not keyword.search(line):
		print line 


# TODO: print lines that contain a word of any length starting with s and ending with e
keyword = re.compile(r'\bs*.e\b')
for line in text:
	if keyword.search(line):
		print line 


# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY
date = raw_input("Please enter a date in the format MM.DD.YY: ")
pattern = re.compile(r'(\d\d).(\d\d).(\d\d)')
d = pattern.search(date)
print "Month: %s \nDay: %s \nYear: %s" % (d.group(1), d.group(2), d.group(3))




# TODO: Write a regular expression that finds html tags in example.html and print them.





# TODO: Scrape a website and search for some things...


