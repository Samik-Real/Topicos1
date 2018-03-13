#PROYECTO FINAL
###############  ########
#Pedro Salazar   00116701
#Javier Caceres
#Samik Real	 00117771
###############  ########

import nltk
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from urllib import request
import re

listabbc = []
prev=''
act=''
def geturlsbbc(prev,num):
    htmlp = request.urlopen("https://www.bbc.co.uk/search?q=bitcoin")
    soup = BeautifulSoup(htmlp)
    for link in soup.findAll('a', attrs={'href': re.compile("^http://www.bbc.co.uk/news/(.*?)")}):
        act=link.get('href')
        if(act!=prev):
            prev=link.get('href')
            listabbc.append(link.get('href'))
            
    print(listabbc)
    #print(soup.get_text())
    print()
    print("Numero de links obtenidos")
    print(len(listabbc)) #muestra el numero de links obtenidos
geturlsbbc(prev,1)

noti=""

for news in listabbc:
    print("Adicionando nueva noticia:")
    htmla =  request.urlopen(news)
    soupart = BeautifulSoup(htmla)
    for articulo in soupart.findAll('h1', attrs={'class': re.compile("story-body__h1")}):
        if articulo.string is not None:
            noti=noti+"\n"+articulo.string
    for articulo in soupart.findAll('div', attrs={'class': re.compile("story-body__inner")}):
        if articulo.text is not None:
            noti=noti+"\n"+articulo.text
    noti=noti+"AAYY0BBZZ"+"\n"
    print("Length actual del String noticia")
    print(len(noti)) #muestra el length del string noticia (que contiene las noticias) despues de adicionar una nueva noticia


from nltk.tokenize import word_tokenize as wtok

tokensi=wtok(noti)
#print(tokensi[:100])
textoi=nltk.Text(tokensi)
type(textoi)
textoi.concordance('bitcoin')
print()

#############################################################################################
listablo = []
act=''
prev=''
def geturlsblo(prev,num):
    htmlp = request.urlopen("https://www.bloomberg.com/search?query=bitcoin")
    soup = BeautifulSoup(htmlp)
    for link in soup.findAll('a', attrs={'href': re.compile("bitcoin")}):
        act=link.get('href')
        if(act!=prev):
            prev=link.get('href')
            listablo.append(link.get('href'))
            
    print(listablo)
    #print(soup.get_text())
    print()
    print("Numero de links obtenidos")
    print(len(listablo)) #muestra el numero de links obtenidos
geturlsblo(prev,1)

noticia=""
for news in listablo:
    print("Adicionando nueva noticia:")
    htmla =  request.urlopen(news)
    soupart = BeautifulSoup(htmla)
    for articulo in soupart.findAll('h1', attrs={'class': re.compile("lede-text-only__hed")}):
        if articulo.string is not None:
            noticia=noticia+"\n"+articulo.string
    for articulo in soupart.findAll('div', attrs={'class': re.compile("body-copy fence-body")}):
        if articulo.text is not None:
            noticia=noticia+"\n"+articulo.text
    noticia=noticia+"AAYY0BBZZ"+"\n"
    print("Length actual del String noticia")
    print(len(noticia)) #muestra el length del string noticia (que contiene las noticias) despues de adicionar una nueva noticia

tokens=wtok(noticia)
#print(tokens[:100])
texto=nltk.Text(tokens)
type(texto)
texto.concordance('bitcoin')
