import bs4
import urllib.request as url
import os

path = "https://www.marvel.com/characters"

response = url.urlopen(path)

if not os.path.exists("images"):
    os.mkdir("images") # make directory

page = bs4.BeautifulSoup(response)
images = page.find_all('img')

for i in range(len(images)):
    src = images[i]['src']
    url.urlretrieve(src, f'images/img_{i}.png')
