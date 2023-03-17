import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for static_file in soup.find_all('link') + soup.find_all('script') + soup.find_all('img'):
    static_url = static_file.get('href') or static_file.get('src')
    if static_url:
        try:
            res = requests.get(static_url)
            if res.status_code != 200:
                print("Failed to load {}. Status code: {}".format(static_url, res.status_code))
            else:
                print("load {} OK".format(static_url))
        except Exception as e:
            print("Failed to load {}. Exception: {}".format(static_url, e))

