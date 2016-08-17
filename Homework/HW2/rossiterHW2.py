from bs4 import BeautifulSoup
import urllib2
import re
import csv



def createRow(link, text, judge_html, page):
	## getting link to pdf
	doc_in_this_div = judge_html.find("div", {"id" : "ContentW"})
	doc_link = doc_in_this_div.find("a", {"class" : "tbprint"})["href"]

	## getting name of judge
	name = link.replace("http://www.judicialwatch.org/document-archive/", "")
	name = name[:-1]
	name = ''.join([i for i in name if not i.isdigit()])
	name = name.replace("-", " ")

	## getting year of report
	year = re.findall(r'\d+', link)
	year = int(year[0])

	row = ({"Page" : page, "Link" : link, "LinktoDoc" : doc_link, "Name": name, "Year" : year, "Text" : text })
	return row


def getJudgeText(link):
	web_page = urllib2.urlopen(link)
	judge_html = BeautifulSoup(web_page.read(), "html.parser")

	try:
		text = judge_html.find("pre").get_text()
	except AttributeError:
		text = "NA"
	finally:
		pass

	## I read the text into a .txt file b/c python was
	## treating it as one string, but as a .txt file,
	## I can read in lines and find sections better w/in
	## the text.
	write_temp_file = open("output.txt", "w")
	write_temp_file.write(text)
	write_temp_file.close()

	read_temp_file = open("output.txt", "r")
	lines = read_temp_file.readlines()
	text_list = []
	for l in lines:
		text_list.append(l)
	read_temp_file.close()

	return judge_html, text_list


def getPageLinks(web_page):
	all_html = BeautifulSoup(web_page.read(), "html.parser")
	fin_disclosures = all_html.find("div", {"id" : "fin_disclosures"})
	html_to_links = fin_disclosures.find_all("span", {"class" : "title"})

	all_links = []
	for l in html_to_links:
		all_links.append(l.find("a", href=True)["href"])
	return all_links


def main():
	with open('judicialWatch.csv', 'wb') as g:	
		w = csv.DictWriter(g, fieldnames=("Page", "Link", "LinktoDoc", "Name", "Year", "Text"))
		w.writeheader()
		for page in range(1, 6):
			start_address = "http://www.judicialwatch.org/judicial-financial-disclosure/page/%s/" % page
			web_page = urllib2.urlopen(start_address)
			page_links = getPageLinks(web_page)
			for link in page_links:
				judge_html, text = getJudgeText(link)
				row = createRow(link, text, judge_html, page)
				w.writerow(row)


main()

  	
