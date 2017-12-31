import requests
import bs4

url = 'http://www.valor.com.br/impresso'

valor_page = requests.get(url)
valor_page.raise_for_status()

valor_page = bs4.BeautifulSoup(valor_page.text, "lxml")

# teaser_titles = valor_page.find_all(class_="teaser-title")
# teasers = valor_page.find_all("div",class_="teaser")


# # print teaser_titles[0].get_text() 
# # esse indice_impresso eh a pagina toda!
# # eh o div pai de todas as manchetes
# indice_impresso = valor_page.find_all("div", class_="indice-impresso")
# h2 = valor_page.find_all("h2", class_="manchete-title")

# if indice_impresso == []:
# 	print 'nada achado'
# else:
# 	for i in range(len(indice_impresso)):
# 		print indice_impresso[i].get_text().strip()
# 		print '-----'*10

# print '\n'*2
# print 'STARTING THE H2'

# if h2 == []:
# 	print 'nenhum h2 achado'
# else:
# 	for i in range(len(h2)):
# 		print h2[i].get_text().strip()
# 		print '-----'*10

# impresso_editorias = valor_page.find_all(class_ = "impresso-editorias")
impresso_editorias = valor_page.find_all(class_ = "impresso-editorias")

for i in range(len(impresso_editorias)):
	noticia_impresso = bs4.BeautifulSoup(str(impresso_editorias[i]), "lxml")

	for j in range(len(noticia_impresso)):
		chapeu_press = noticia_impresso.find(class_ = "chapeu-press")
		manchete_title = noticia_impresso.find(class_ = "manchete-title")
		teaser = noticia_impresso.find(class_ = "teaser")

		if chapeu_press.get_text() != '':
			print str(i) + '. [' + chapeu_press.get_text() + ' - ' + manchete_title.get_text().strip() + ']'
		else:
			print str(i) + '. [' + manchete_title.get_text().strip() + ']'
		print teaser.get_text().strip()
		print '\n' + '---'*20

# a = impresso_editorias[0]
# r = bs4.BeautifulSoup(str(a), "lxml")
# teaser = r.find_all(class_ = "teaser")
# print teaser



