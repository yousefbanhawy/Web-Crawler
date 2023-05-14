import requests
from bs4 import BeautifulSoup
import time
url = 'https://www.freecodecamp.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    Link = link.get('href')
    time.sleep(0.1)
    if link.get('href') != None:
        if 'https://' in link.get('href'):
            print(link.get('href'))
        else:
              print('https://www.freecodecamp.org/' + Link)  # Convert relative URL to absolute URL