from requests import get
from bs4 import BeautifulSoup

def url_content(url):
    response = get(url)
    return response.content

if __name__ == '__main__':
    url = 'https://www.rotundastore.com/catalogo/nust-brick_12130153_06'
    #print(url_content(url))

    soup = BeautifulSoup(url_content(url), 'html.parser')
    results = soup.find(id='lstTalles')
    print(results.prettify())