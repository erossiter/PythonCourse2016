from bs4 import BeautifulSoup
import urllib2
import re
import csv
#import time
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys



#def getText(link):
	#chromeOptions = webdriver.ChromeOptions()
	#prefs = {"download.default_directory" : "/Users/erinrossiter/Dropbox/Summer2016/PythonCourse2016/Homework/HW2"}
	#chromeOptions.add_experimental_option("prefs", prefs)
	#chromedriver = "/usr/local/bin/chromedriver"
	#driver = webdriver.Chrome(executable_path = chromedriver, chrome_options = chromeOptions)

	#driver.get("http://document.online-convert.com/convert-to-txt")
	#input_element = driver.find_element_by_name("external_url")
	#input_element.send_keys(link)
	#driver.find_element_by_id("submit_button").click()

	#driver.switch_to.frame(0)
	## I just need to get on this page and then I can work with the page source!!

	#print driver.current_url
	#driver.close()

	#driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
	#driver.switch_to_default_content()
	#driver.find_element_by_link_text('direct download link').click()


	#language = driver.find_element_by_id('language_box')
	#language.click()
	#print driver.current_url
	#print driver.page_source
#	driver.close()
	#print driver.current_url
	#driver.find_element(by = By.LINK_TEXT, value = "direct download link").click()
	#download_link = driver.find_element_by_xpath('//*[@id="download_box"]/strong/a')
	#download_link.click()
	#driver.close()
	



def createRow(link, text, judge_html):
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

	row = ({"Link" : link, "LinktoDoc" : doc_link, "Name": name, "Year" : year, "Text" : text })
	return row


def getJudgeText(link):
	web_page = urllib2.urlopen(link)
	judge_html = BeautifulSoup(web_page.read(), "html.parser")
	gen_text = judge_html.find("div", {"id" : "DAAGT"})
	text = gen_text.find("pre").get_text()

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
		w = csv.DictWriter(g, fieldnames=("Link", "LinktoDoc", "Name", "Year", "Text"))
		w.writeheader()
		for i in range(1, 50):
			start_address = "http://www.judicialwatch.org/judicial-financial-disclosure/page/%s/" % i
			web_page = urllib2.urlopen(start_address)
			page_links = getPageLinks(web_page)
			for link in page_links:
				judge_html, text = getJudgeText(link)
				row = createRow(link, text, judge_html)
				w.writerow(row)


main()

  	
