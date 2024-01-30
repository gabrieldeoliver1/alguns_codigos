from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def limpar_texto(texto):
    texto = texto.strip()
    texto_limpo = []
    # Trocando um ou mais caracteres de nova linha (enter) por um espaço.
    texto = re.sub("\n+", " ", texto)
    # Trocando um ou mais espaços por um espaço.
    texto = re.sub(" +", " ", texto)
    # Remover os caracteres de controle
    texto = texto.replace(u'\xa0', u'')
    # Remover números entre colchetes (citações Wikipedia)
    texto = re.sub("\[[0-9]*\]", "", texto)
    texto = texto.split(" ")
    for item in texto:
        item = item.strip()
        # string.punctuation == '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        # Removendo caracteres de pontuação antes e depois da string
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'e' or item.lower() == 'o'):
            texto_limpo.append(item)

    return texto_limpo

html = urlopen("https://pt.wikipedia.org/wiki/Python")
bsObj = BeautifulSoup(html)
conteudo = bsObj.find("div", {"id":"mw-content-text"}).get_text()
conteudo = limpar_texto(conteudo)
print(conteudo)


