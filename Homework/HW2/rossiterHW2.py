from bs4 import BeautifulSoup
import urllib2

import csv


def getPDF(link):
	all_html = BeautifulSoup(link.read())
	gen_text = all_html.find("div", {"id" : "DAAGT"})
	return gen_text.find("pre").get_text()


def getPageLinks(web_page):
	all_html = BeautifulSoup(web_page.read())
	fin_disclosures = all_html.find("div", {"id" : "fin_disclosures"})
	html_to_links = fin_disclosures.find_all("span", {"class" : "title"})

	all_links = []
	for l in html_to_links:
		all_links.append(l.find("a", href=True)["href"])
	return all_links


def main():
	#for i in range(1, 2):
		start_address = "http://www.judicialwatch.org/judicial-financial-disclosure/page/%s/" % 1
		web_page = urllib2.urlopen(start_address)
		page_links = getPageLinks(web_page)
		for link in page_links:
			link = urllib2.urlopen(link)
			x = getPDF(x)#x now holds all the text from the pdf 



		with open('judicialWatch.csv', 'wb') as g:	
			w = csv.DictWriter(g, fieldnames=("Name", "Year", "Link", "Text"))
			w.writeheader()


main()

  	
