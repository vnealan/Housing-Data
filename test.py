import urllib2
from bs4 import BeautifulSoup
soup = BeautifulSoup(urllib2.urlopen('http://www.realestate.com.au/sold/property-apartment-in-maroubra%2c+nsw+2035/list-1?source=refinements').read())

for price in soup.find_all('li',"first"):
	print(price.get_text())