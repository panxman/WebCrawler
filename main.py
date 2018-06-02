import requests
from bs4 import BeautifulSoup
import pandas


def trade_spider(max_pages):
    page = 1
    item_list = []
    while page <= max_pages:
        url = 'http://www.skroutz.gr/c/40/kinhta-thlefwna.html?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        # Find all the Divs with Class DETAILS
        divs = soup.find_all('div', {'class': 'details'})
        for x in divs:
            item_dict = {}
            headers = x.find_all('h2')
            for y in headers:
                links = y.find_all('a')
                for z in links:
                    href = 'http://www.skroutz.gr/' + z.get('href')
                    title = z.string
                    print(href)
                    print(title)
                    item_dict["Link"] = href
                    item_dict["Title"] = title
            item_list.append(item_dict)
        page += 1
    dataFrame = pandas.DataFrame(item_list)
    dataFrame.to_csv("Items.csv")


trade_spider(3)
