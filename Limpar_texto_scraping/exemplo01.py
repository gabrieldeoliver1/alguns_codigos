from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pt.wikipedia.org/wiki/Python")
bsObj = BeautifulSoup(html)
conteudo = bsObj.find("div", {"id":"mw-content-text"}).get_text()
conteudo = conteudo.split(" ")
print(conteudo)