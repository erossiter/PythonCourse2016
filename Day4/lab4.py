#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
	

from bs4 import BeautifulSoup
import urllib2
import re
import csv

with open('profs.csv', 'wb') as f:
	w = csv.DictWriter(f, fieldnames=("Name", "Specialization", "Title", "E-mail", "Web page"))
	w.writeheader()

	web_address='https://polisci.wustl.edu/faculty/specialization'
	web_page = urllib2.urlopen(web_address)

	all_html = BeautifulSoup(web_page.read())
	all_div = all_html.find_all("div")

	for i in range(49, 85):
		extension = all_div[i].find('a')['href']
		title = all_div[i].contents[2]
		name = all_div[i].find('a').get_text()

		prof_address = 'https://polisci.wustl.edu%s' % extension
		prof_page = urllib2.urlopen(prof_address)
		prof_html = BeautifulSoup(prof_page.read())

		check_this_div = prof_html.find("div", {"class" : "field field-name-field-person-email field-type-email field-label-inline clearfix"})
		check_these_a = check_this_div.find_all("div", {"class" : "field-item even"})
		for a in check_these_a:
			if a.find("a", href=True):
				email = a.get_text()
			else:
				email = "NA"

		check_this_div = prof_html.find("div", {"class" : "field field-name-field-person-website field-type-link-field field-label-inline clearfix"})
		if check_this_div:
			web_page = check_this_div.find("a", href=True)['href']
		else:
			web_page = "NA"


		results = prof_html.find_all("a", {"property" : "rdfs:label skos:prefLabel"})
		add_fields = []
		for r in results:
			r = r.get_text()
			fields = ["Political Theory", "American", "Methodology", "Comparative", "International Political Economy", "Formal Theory"]
			if r in fields:
				add_fields.append(r)
		specialization = ", ".join(add_fields)

  		w.writerow({"Name" : name, "Specialization" : specialization, "Title" : title, "E-mail" : email, "Web page" : web_page})


	


	