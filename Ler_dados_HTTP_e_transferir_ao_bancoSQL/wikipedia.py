from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import mysql.connector
import re

dados_conexao = {"user":"root", "password":"1234", "host":"127.0.0.1", "database":"scraping", "charset":"utf8"}
conexao = mysql.connector.connect(**dados_conexao)
cursor = conexao.cursor()

def gravar(titulo, url, conteudo):
    cursor.execute('INSERT INTO paginas (titulo, url, conteudo)'
                   'VALUES (%s, %s, %s)', (titulo, url, conteudo))
    conexao.commit()

def getLinks(urlArtigo):
    url = 'http://pt.wikipedia.org'+urlArtigo
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    titulo = bs.find('h1').get_text()
    conteudo = bs.find('div', {'id':'mw-content-text'}).find('p').get_text()
    gravar(titulo, url, conteudo)
    return bs.find('div', {'id':'bodyContent'}).\
        findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

# ^ -> Indica o início da string
# (/wiki/) -> Contenha /wiki/
# ((?!:) -> Afirmação negativa para não pegar ":"
# . -> Qualquer caractere
# )* -> Em qualquer quantidade
# $ -> Indica o final da string
# Exemplo:
# <a href="/wiki/Wikip%C3%A9dia:Boas-vindas">Boas-vindas</a>
# Vai pegar: "/wiki/Wikip%C3%A9dia"

links = getLinks('/wiki/Copa_do_Mundo_FIFA_de_2026')
for link in links:
    print("Link: " + link)

try:
    contador = 1
    while len(links) > 0 and contador <= 10:
        novoArtigo = links[random.randint(0, len(links)-1)].attrs['href']
        print(str(contador) + " -> " + novoArtigo)
        links = getLinks(novoArtigo)
        for link in links:
            print("Link: " + link)
        contador += 1
finally:
    cursor.close()
    conexao.close()