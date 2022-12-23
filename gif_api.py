import json
from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"

params = parse.urlencode({
  "q": "tom and jerry",
  "api_key": "bc56161131654faeb550630b83e0c977",
  "limit": "20"
})

path = "".join((url, "?", params))
response = request.urlopen(path)
data = json.load(response)
images = data['data']
for i in range(len(images)):
    path = images[i]['images']['original']['url']
    request.urlretrieve(path, f'images/img_{i}.gif')
    print(f"Downloaded : {i+1} images",)
