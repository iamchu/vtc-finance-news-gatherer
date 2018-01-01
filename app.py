import requests
import bs4

def main():
	print 'Wish a specific url_suffix (for valor)? Enter nothing if you don\'t.'
	url_suffix = raw_input()
	getNewsFromValor(url_suffix)

def getNewsFromValor(url_suffix = ''):
	import requests
	import bs4
	news_index_count = 0
	url = 'http://www.valor.com.br/impresso/' + url_suffix

	valor_page = requests.get(url)
	valor_page.raise_for_status()
	valor_page = bs4.BeautifulSoup(valor_page.text, "lxml")

	impresso_editorias = valor_page.find_all(class_ = "impresso-editorias")

	for i in range(len(impresso_editorias)):
		print '\n'
		section_with_noticia_impresso = bs4.BeautifulSoup(str(impresso_editorias[i]), "lxml")

		# TITULO DO CADERNO
		print '*********** ' + section_with_noticia_impresso.find(class_ = "section-title").get_text() + ' ***********'
		print '\n'

		for j in range(len(section_with_noticia_impresso)):
			noticia_impresso = section_with_noticia_impresso.find_all(class_ = "noticia-impresso")

			for g in range(len(noticia_impresso)):
				news_index_count+=1

				unidade_de_noticia = bs4.BeautifulSoup(str(noticia_impresso[g]), "lxml")

				chapeu_press = unidade_de_noticia.find(class_ = "chapeu-press")
				manchete_title = unidade_de_noticia.find(class_ = "manchete-title")
				teaser = unidade_de_noticia.find(class_ = "teaser")
				link = unidade_de_noticia.find('a')

				if chapeu_press.get_text() != '':
					print str(news_index_count) + '. [' + chapeu_press.get_text() + ' - ' + manchete_title.get_text().strip() + ']'
				else:

					print str(news_index_count) + '. [' + manchete_title.get_text().strip() + ']'
				print teaser.get_text().strip() + '\n'
				print('http://www.valor.com.br/' + link.get('href')).strip()
				print '\n' + '---'*20

# obs: checar se tem o caderno. se nao tiver, proceder de acordo
def createHtml(caderno, title, teaser):
	return

main()
