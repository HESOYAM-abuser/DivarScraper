import re 
import requests
from bs4 import BeautifulSoup, SoupStrainer

def city_links():
    url = 'https://www.divar.ir/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    project_href = [i['href'] for i in soup.find_all('a', href=True)]
    links = list(dict.fromkeys(project_href))
    clean_links = []
    for i in links:
        if re.search("/s/", i):
            clean_links.append(i)
        else:
            pass
    return clean_links

if __name__ == "__main__":
    with open('city.txt', 'w') as f:
        for i in city_links():
            f.write(i+'\n')