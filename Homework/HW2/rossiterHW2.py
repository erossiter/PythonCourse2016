from bs4 import BeautifulSoup
import urllib2

import csv



def searchJudge(asG, html):
	#fin_disclosures = all_html.find("div", {"id" : "fin_disclosures"})
	#html_to_links = fin_disclosures.find_all("span", {"class" : "title"})

	all_links = []
	for l in html_to_links:
		all_links.append(l.find("a", href=True)["href"])

def checkJudge(asF):
	first_name, middle_int, last_name, conf_year = judgeInfo(asF)
	if conf_year < 2013:
		return "%s %s. %s" % (first_name, middle_int, last_name)
	else:
		return None


def judgeInfo(asF):
	my_reader = csv.reader(asF)
  	my_reader.next()
  	x = my_reader.next()
  	last_name = x[1]
  	first_name = x[2]
  	middle_name = x[3]
  	confirmation = x[37]
  	return first_name, middle_name[0], last_name, int(confirmation[6:])


def main():
	with open("federalJudges.csv", 'rb') as f:
		for i in range(0, 10):
			print checkJudge(asF=f)

	with open('judicialWatch.csv', 'wb') as g:
		w = csv.DictWriter(g, fieldnames=("Name", "Year", "Link"))
		w.writeheader()

		web_address = "http://www.judicialwatch.org/judicial-financial-disclosure/?q="
		web_page = urllib2.urlopen(web_address)
		all_html = BeautifulSoup(web_page.read())

		searchJudge(g, all_html)




main()

  	
