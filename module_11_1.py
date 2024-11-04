from bs4 import BeautifulSoup
import requests

URL = 'https://ru.wikipedia.org/wiki/%D0%A3%D1%82%D0%BA%D0%B8'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

for data in soup.select('.mw-content-ltr p'):
    num_words_in_line = 0
    text = ''

    for word in data.text.split(' '):
        text += word + ' '
        num_words_in_line += 1

        if num_words_in_line == 12:
            num_words_in_line = 0
            text += '\n'

    print(text)
