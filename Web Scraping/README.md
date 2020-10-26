# Web Scraping with Python
Importing useful libraries i.e requests and bs4
```python
import requests
link = requests.get("http://www.example.com")
```
```python
import bs4
soup = bs4.BeautifulSoup(link.text,'lxml')
print(soup)
```
Output
```html
<!DOCTYPE html>
<html>
<head>
<title>Example Domain</title>
<meta charset="utf-8"/>
<meta content="text/html; charset=utf-8" http-equiv="Content-type"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>
<body>
<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```
Navigating through the soup
```python
soup.select('title')            # [<title>Example Domain</title>]
title_tag = soup.select('title')
title_tag[0]                    # <title>Example Domain</title>
title_tag[0].getText()          # 'Example Domain'
```
### Grabbing an Image
Find the image class name
```python
image_info = soup.select('.ImageClassName')

pic1 = image_info[0]

# grabbing the link of image
pic1['src']

image_link = requests.get('link_of_the_image')

# The raw content (its a binary file, meaning we will need to use binary read/write methods for saving it)
image_link.content
```
#### Saving the grabbed image
```python
file = open('new_file_name.jpg/png/whatever','wb')
file.write(image_link.content)
f.close()
```