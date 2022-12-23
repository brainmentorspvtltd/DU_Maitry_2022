import bs4
import urllib.request as url

productName = input("Search Product : ")
productName = productName.replace(" ","+")
path = f"https://www.flipkart.com/search?q={productName}"

response = url.urlopen(path)   # Making HTTPRequest to Flipkart...
page = bs4.BeautifulSoup(response)

titleList = page.find_all('div', {'class' : '_4rR01T'})
priceList = page.find_all('div', {'class' : '_30jeq3 _1_WHN1'})
ratingsList = page.find_all('span', {'class' : '_2_R_DZ'})
for i in range(len(titleList)):
    print("Title :",titleList[i].text)
    print("Price :",priceList[i].text)
    print("Reviews :",ratingsList[i].text)
    print("*" * 40)
