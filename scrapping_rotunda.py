from requests import get
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import json
import time

def url_content(url, headers=None):
    response = get(url, headers= headers)
    return response.content

if __name__ == '__main__':
    url = input("URL: ")
    
    agent = UserAgent()
    header = {'User-Agent': agent.random}
    website = url_content(url,header)
    # website_content = BeautifulSoup(website, "html.parser")
    pattern = re.compile(r'"sizes":.+?(?=])')
    match = pattern.search(str(website))
    if match:
        string_lst = match.group().split('"sizes":', maxsplit=1)[-1] + ']'
        result_json = json.loads(string_lst)
        for item in result_json:
            print(f"Talle: {item['name']} --> {item['availability']}")
    