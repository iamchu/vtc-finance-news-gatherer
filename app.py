# * resolver bug que pega tema e titulo como mesma coisa 
# pegar o parent do teaser-title e do title, fica mais facil de manipular

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

	teaser_titles = valor_page.find_all("div",class_="teaser-title")
	teasers = valor_page.find_all("div",class_="teaser")
	if teaser_titles == []:
		print 'no titles found'
	else:
		for i in range(len(teaser_titles)):
			print  '[' + teaser_titles[i].get_text().strip() + ']'
			if teasers[i]:
				print teasers[i].get_text().strip()
			print '-----'*3
		# for i in range(len(teasers)):
			# print teasers[i].get_text()

	# print valor_page.text

main()
