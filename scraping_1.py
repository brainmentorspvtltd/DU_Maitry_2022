import bs4
import urllib.request as url

path = "https://www.flipkart.com/search?q=APPLE+WatCH+SmART"

response = url.urlopen(path)   # Making HTTPRequest to Flipkart...
page = bs4.BeautifulSoup(response)
title = page.find('div', {'class' : '_4rR01T'})
price = page.find('div', {'class' : '_30jeq3 _1_WHN1'})
print(title.text)
print(price.text)
