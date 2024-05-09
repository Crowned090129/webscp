import os
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# url = 'https://www.health.harvard.edu/a-through-c#A-terms'
BASE_URL = 'https://www.health.harvard.edu/'
GROUPS = ['a-through-c#', 'd-through-i#', 'j-through-p#', 'q-through-z#']
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M',
           'N', 'L', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# BRING IT ALL


def getData(url):
    s = HTMLSession()
    return BeautifulSoup(s.get(url).text, 'html.parser')

# SELECTING SPECIFIC WORDS


def getWords(soup):
    return soup.select('p > strong')

# FUNCTION TO CLEAN DATA


def work():
    words = []
    for group in GROUPS:
        for word in getWords(getData(BASE_URL + group)):
            if word.has_attr('class') and 'leading-tight' in word['class']:
                break
            elif 'Sign up' in word.parent.get_text():
                break
            elif 'The Best Diets' in word.parent.get_text():
                break
            elif 'Get helpful' in word.parent.get_text():
                break
            else:
                print(word.parent)
                words.append(word.parent)
    return words


# DO THE WORK
terms = work()

# CHECK IF FILE EXISTS
FILE_PATH = (
    r'data.txt')
if os.path.exists(FILE_PATH):
    os.remove(FILE_PATH)

# WRITE TO FILE
with open(r'data.txt', 'w', encoding='utf-8') as f:
    for element in terms:
        f.write(element.get_text() + '\n')
