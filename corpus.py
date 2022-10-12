# Gabriel Antonio Gomes de Farias
'''
ENUNCIADO 
Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de 
linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função 
que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta 
url. Duas condições são importantes:  
a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 
1000 palavras.  
b) O texto desta página deverá ser transformado em um array de senteças.  
 
Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca 
Spacy. 
'''
import requests
from bs4 import BeautifulSoup, Comment
import spacy

nlp = spacy.load("en_core_web_sm")  # carrega modulo ingles

# 5 sites em ingles p/processar
url1 = 'https://en.wikipedia.org/wiki/Natural_language_processing'
url2 = 'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html'
url3 = 'https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP'
url4 = 'https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1'
url5 = 'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/'

urls = [url1, url2, url3, url4, url5]

# vetores vazios para ser encaminhado os textos das paginas
texto1 = []
texto2 = []
texto3 = []
texto4 = []
texto5 = []


def filtraTexto(element):
  if element.parent.name in [
      'style', 'script', 'head', 'title', 'meta', '[document]'
  ]:
    return False
  if isinstance(element, Comment):
    return False
  return True


op = 0
qUrl = len(urls)  # qtd links

while op < qUrl:
  html = requests.get(urls[op]).text
  soup = BeautifulSoup(html, 'html.parser')
  texts = soup.findAll(text=True)
  textFiltrado = filter(filtraTexto, texts)
  text = " ".join(t.strip() for t in textFiltrado)
  page = nlp(text)
  for sentence in page.sents:
    if op == 0:
      texto1.append(sentence.text)
    elif op == 1:
      texto2.append(sentence.text)
    elif op == 2:
      texto3.append(sentence.text)
    elif op == 3:
      texto4.append(sentence.text)
    elif op == 4:
      texto5.append(sentence.text)

  op += 1

print(texto1)
print(texto2)
print(texto3)
print(texto4)
print(texto5)
