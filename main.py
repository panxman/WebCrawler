import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.skroutz.gr/c/40/kinhta-thlefwna.html?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        divs = soup.find_all('div', {'class': 'details'})  # Find all the Divs with Class DETAILS
        for x in divs:
            headers = x.find_all('h2')
            for y in headers:
                links = y.find_all('a')
                for z in links:
                    href = 'http://www.skroutz.gr/' + z.get('href')
                    title = z.string
                    print(href)
                    print(title)
        page += 1

trade_spider(3)
