import os
import requests
import bs4

def main():
	getTitles()

# gets all titles and returns as list
def getTitles():
	url = 'http://www.valor.com.br/impresso'

	valor_page = requests.get(url)
	valor_page.raise_for_status()

	valor_page = bs4.BeautifulSoup(valor_page.text)

	titles = valor_page.find_all("div",class_="teaser")
	if titles == []:
		print 'no titles found'
	else:
		for i in range(len(titles)):
			print titles[i]
			print '\n'

	# print valor_page.text

main()
