from bs4 import BeautifulSoup
import urllib2

import csv


def gotoLink(link):


def searchJudge(web_page):
	all_html = BeautifulSoup(web_page.read())
	fin_disclosures = all_html.find("div", {"id" : "fin_disclosures"})
	html_to_links = fin_disclosures.find_all("span", {"class" : "title"})

	all_links = []
	for l in html_to_links:
		all_links.append(l.find("a", href=True)["href"])
	return all_links


def checkJudge(asF):
	my_reader = csv.reader(asF)
  	my_reader.next()
  	x = my_reader.next()
  	last_name = x[1]
  	first_name = x[2]
  	middle_int = x[3][0]
  	confirmation_year = int(x[37][6:])

	if confirmation_year < 2013:
		return "%s+%s.+%s" % (first_name, middle_int, last_name)
	else:
		return None


def main():
	with open("federalJudges.csv", 'rb') as f:
		for i in range(0, 10):
			the_judge = checkJudge(asF=f)
			if the_judge != None:
				start_address = "http://www.judicialwatch.org/judicial-financial-disclosure/?q=" + the_judge
				web_page = urllib2.urlopen(start_address)
				searchJudge(web_page)


	#with open('judicialWatch.csv', 'wb') as g:	
	#	w = csv.DictWriter(g, fieldnames=("Name", "Year", "Link"))
	#	w.writeheader()


main()

  	
