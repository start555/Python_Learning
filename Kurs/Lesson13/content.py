#Распарсить страницу https://docs.python.org/3/library/index.html. Извлечь оглавление в удобочитаемом виде.

from urllib import request
from bs4 import BeautifulSoup

url = "https://docs.python.org/3/library/index.html"
html_doc = request.urlopen(url)
soup = BeautifulSoup(html_doc, "html.parser")

for i in soup.find_all("li", attrs={"class": "toctree-l1"}):
    print(i.get_text())