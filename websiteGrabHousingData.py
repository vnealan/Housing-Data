import urllib2
from bs4 import BeautifulSoup

# http://www.realestate.com.au/sold/property-apartment-with-studio-in-kensington%2c+nsw+2033/list-1?maxBeds=any&includeSurrounding=false&source=refinements
# http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-with-studio-in-maroubra%2c+nsw+2035/list-1?maxBeds=any&includeSurrounding=false&misc=ex-no-sale-price&activeSort=list-date&source=refinements


where='maroubra'
urlPartOne='http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-with-studio-in-maroubra%2c+nsw+2035/list-'
urlPartTwo='?maxBeds=any&includeSurrounding=false&misc=ex-no-sale-price&activeSort=list-date&source=refinements'

# where='kensington'
# urlPartOne='http://www.realestate.com.au/sold/property-apartment-with-studio-in-kensington%2c+nsw+2033/list-'
# urlPartTwo='?maxBeds=any&includeSurrounding=false&source=refinements'

# where='laneCove'
# urlPartOne='http://www.realestate.com.au/sold/property-apartment-in-lane+cove%2c+nsw+2066/list-'
# urlPartTwo='?source=location-search'

# where='laneCoveNorth'
# urlPartOne='http://www.realestate.com.au/sold/property-apartment-in-lane+cove+north%2c+nsw+2066%3b+/list-'
# urlPartTwo='?source=location-search'


text_file = open(where+"price.txt", "w")
# obs=1
for x in range(0,75):
	y=str(x)
	soup = BeautifulSoup(urllib2.urlopen(urlPartOne+y+urlPartTwo).read())
	for price in soup.find_all('p',"price"):
# 		obs_text = str(obs)
		text_file.write(price.get_text()+"\n")
		# print(price.get_text())
		# print("#"+obs_text+" "+price.get_text())
# 		obs=obs+1
text_file.close()

text_file = open(where+"soldDate.txt", "w")
# obs=1
for x in range(0,75):
	y=str(x)
	soup = BeautifulSoup(urllib2.urlopen(urlPartOne+y+urlPartTwo).read())
	for soldDate in soup.find_all('p','soldDate'):
# 		obs_text = str(obs)
		text_file.write(soldDate.get_text()+"\n")
		# print(soldDate.get_text())
# 		print("#"+obs_text+" "+soldDate.get_text())
# 		obs=obs+1
text_file.close()

text_file = open(where+"location.txt", "w")
# obs=1	
for x in range(0,75):
	y=str(x)
	soup = BeautifulSoup(urllib2.urlopen(urlPartOne+y+urlPartTwo).read())
	for location in soup.find_all('a','name'):
# 		obs_text = str(obs)
		text_file.write(location.get_text()+"\n")
		# print(location.get_text())
# 		print("#"+obs_text+" "+location.get_text())
# 		obs=obs+1
text_file.close()

text_file = open(where+"bedroom.txt", "w")
# obs=1	
for x in range(0,75):
	y=str(x)
	soup = BeautifulSoup(urllib2.urlopen(urlPartOne+y+urlPartTwo).read())
	for bedroom in soup.find_all('img',alt="Bedrooms"):
# 		obs_text = str(obs)
		text_file.write(bedroom.next_sibling.get_text()+"\n")
		# print(bedroom.next_sibling.get_text())
# 		print("#"+obs_text+" "+bedroom.next_sibling.get_text())
# 		obs=obs+1
text_file.close()

	# for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
	#     tds = row('td')
	#     print tds[0].string, tds[1].string