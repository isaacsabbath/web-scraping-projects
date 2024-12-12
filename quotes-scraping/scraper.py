import requests
import quopri # Decodes the file into hmtl format

from bs4 import BeautifulSoup

# When you download the html Encoding errors will be faced 
# with open('index.html', 'r') as fp:
# 	contents = fp.read()

# 	# Encoding issues used the quopri 
# 	response = quopri.decodestring(contents).decode('utf-8')

# 	soup = BeautifulSoup(response, 'lxml')

# 	quotes = soup.find_all('div', class_="quote")
# 	for quote in quotes:
# 		quote_text = quote.span.text
# 		author = quote.small.text

# 		print(f"quote: {quote_text}")
# 		print(f"Author: {author}")
# 		print("-"*50)

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
	quote_text = quote.span.text
	author = quote.small.text

	print(f"quote: {quote_text}")
	print(f"Author: {author}")
	print("-"*50)
	
	

