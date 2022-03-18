KEYWORDS = ['дизайн', 'фото', 'web', 'python']

import requests
import bs4

url = 'https://habr.com/ru/all/'

headers = {
    'user-agent': 'something'
}

responce = requests.get(url, headers=headers)
responce.raise_for_status()
text = responce.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for elements in articles:
    for key in KEYWORDS:
        if key in elements.text:
            article = elements.find(class_='tm-article-snippet__title-link').find('span')
            href = elements.find(class_='tm-article-snippet__title-link').attrs['href']
            datetime = elements.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
            info = elements.find(class_='tm-article-body tm-article-snippet__lead')
            print(f'<{datetime}> - <{article.text}> - <{url + href}>')