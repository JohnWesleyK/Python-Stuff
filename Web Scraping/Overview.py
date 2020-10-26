import requests
result = requests.get("http://www.example.com")
# print(result.text)

import bs4
soup = bs4.BeautifulSoup(result.text,"lxml")

# print(soup.select('title'))     # [<title>Example Domain</title>]
# print(soup.select('p'))

# '''
# [<p>This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.</p>, <p><a href="https://www.iana.org/domains/example">More information...</a></p>]
# '''
# print(soup.select('h1'))    # [<h1>Example Domain</h1>]

# print(soup.select('title')[0].getText())
# paragraph = soup.select('p')[0].getText()
# print(paragraph)

# Grabbing classes
res = requests.get("https://en.wikipedia.org/wiki/Aimer")
soup = bs4.BeautifulSoup(res.text,"lxml")
# print(soup)
# print(soup.select('.toctext'))
first_item = soup.select('.toctext')[0]
# print(first_item.text)
# for item in soup.select('.toctext'):
#     print(item.text)

# Grabbing an Image
res1 = requests.get("https://en.wikipedia.org/wiki/Overlord_(2018_film)")
soup1 = bs4.BeautifulSoup(res1.text,"lxml")
overlord = soup1.select('img')[0]
# print(overlord)
# print(overlord['src'])
image_link = requests.get('https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/Overlord2018Poster.jpg/220px-Overlord2018Poster.jpg')
# print(image_link.content)
f = open('overlord.png','wb')
f.write(image_link.content)
f.close()

res = requests.get("https://en.wikipedia.org/wiki/Aimer")
soup = bs4.BeautifulSoup(res.text,"lxml")
aimer = soup.select('img')[0]
# print(aimer['src'])
aimer_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Aimer_live.png/220px-Aimer_live.png')
# print(aimer_link.content)
f = open('aimer.png','wb')
f.write(aimer_link.content)
f.close()