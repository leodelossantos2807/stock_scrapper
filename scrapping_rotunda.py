from requests import get
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def url_content(url, headers=None):
    response = get(url, headers= headers)
    return response.content

if __name__ == '__main__':
    url = 'https://www.zara.com/uy/es/sobrecamisa-cuadros-p06023519.html?v1=95823853&v2=1723554'
    agent = UserAgent()
    header = {'User-Agent': agent.random}
    soup = BeautifulSoup(url_content(url,header), 'html.parser')
    print(soup.prettify())