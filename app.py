import requests
import bs4

def main():
	getNewsFromValor()

# gets all titles and returns as list (?????)
def getNewsFromValor():
	import requests
	import bs4

	url = 'http://www.valor.com.br/impresso'

	valor_page = requests.get(url)
	valor_page.raise_for_status()
	valor_page = bs4.BeautifulSoup(valor_page.text, "lxml")

	# returns a list containing all impresso_editorias in valor_page
	impresso_editorias = valor_page.find_all(class_ = "impresso-editorias")

	for i in range(len(impresso_editorias)):

		# this should be nameed someting else!! Because there are multiple noticia-impresso in each of
		# impresso-editorias!
		# what we need to do is grab each noticia-impresso from each impresso-editorias. 
		# There will be multiple noticia-impresso! 
		# we'll probably need to use another bs4

		# returns a list of the impresso-editorias
		noticia_impresso = bs4.BeautifulSoup(str(impresso_editorias[i]), "lxml")

		for j in range(len(noticia_impresso)):

			chapeu_press = noticia_impresso.find(class_ = "chapeu-press")
			manchete_title = noticia_impresso.find(class_ = "manchete-title")
			teaser = noticia_impresso.find(class_ = "teaser")

			if chapeu_press.get_text() != '':
				print str(i+1) + '. [' + chapeu_press.get_text() + ' - ' + manchete_title.get_text().strip() + ']'
			else:

				print str(i+1) + '. [' + manchete_title.get_text().strip() + ']'
			print teaser.get_text().strip()
			print '\n' + '---'*20

main()
