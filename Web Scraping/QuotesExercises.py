import requests
import bs4

base_url = 'http://quotes.toscrape.com/page/{}/'

authors = []
literal_quotes = []

# task 1,2
for n in range (1,11):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    quotes = soup.select(".quote")

    for quote in quotes:
        # print(quote.select('.text')[0].getText())

        author = quote.select('.author')[0].getText()
        authors.append(author)

        literal_quote = quote.select('.text')[0].getText()
        literal_quotes.append(literal_quote)


# print(authors)
# print(literal_quotes)

# task 3
top_ten_tags = []
scrape_url = base_url.format(10)
res = requests.get(scrape_url)

soup = bs4.BeautifulSoup(res.text, 'lxml')

for i in range(10):
    tag = soup.select(".tag-item")[i].getText()
    top_ten_tags.append(tag)

for tag in top_ten_tags:
    print(tag)

# task 4
unique_authors = []
for n in range (1,11):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    quotes = soup.select(".quote")

    for quote in quotes:
        # print(quote.select('.text')[0].getText())

        unique_author = quote.select('.author')[0].getText()
        if unique_author not in unique_authors:
            unique_authors.append(unique_author)

print(len(unique_authors))
