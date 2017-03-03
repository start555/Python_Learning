#Распарсить страницу http://www.tc.belhard.com/courses/courses2.php.
# Извлечь все ссылки на описания курсов. Пройти по каждой ссылке и извлечь оглавление каждого курса.
import re
from urllib import request
from bs4 import BeautifulSoup

url = "http://www.tc.belhard.com/courses/courses2.php"
html_doc = request.urlopen(url)
soup = BeautifulSoup(html_doc, "html.parser")

# функция получения url (ссылок) на все курсы (сохраняем в set, чтобы избавится от повторов)
def getCourseUrls():
    course_links_set = set()
    for i in soup.findChildren("a", attrs={"href": re.compile(r"courselist/kursy|\d\d.php")}):
        course_links_set.add(i["href"])
    course_urls_list = list(course_links_set)
    return course_urls_list

# функция для получения оглавления по каждому из курсов
def getCourseTopics(lst):
    for url in lst:
        html_doc = request.urlopen(url)
        soup = BeautifulSoup(html_doc, "html.parser")
        course_program = set()
        for topic in soup.find_all(text=re.compile(r"Занятие|Тема")):
            course_program.add(topic)
    return list(course_program)