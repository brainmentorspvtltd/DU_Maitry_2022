import bs4
import urllib.request as url

path = "https://www.rottentomatoes.com/m/kgf_chapter_2"

response = url.urlopen(path)
page = bs4.BeautifulSoup(response)

movieTitle = page.find('h1', {'class' : 'scoreboard__title'})
info = page.find('p', {'class': 'scoreboard__info'})
print(movieTitle.text)
print(info.text)
