from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import re

my_url = 'https://www.newegg.com/p/pl?N=100252375&ActiveSearchResult=True&SrchInDesc=pokemon'

#opens connection & grabs html page
uClient = uReq(my_url)

#offloads webpage content into variable
page_html = uClient.read()
uClient.close()

#html parsing
page_soup= soup(page_html, "html.parser")

#page_soup.h1
#page_soup.p
#page_soup.body.span

#grabs each product
containers = page_soup.findAll("div", {"class": {"item-container"}})

#gets num of products
# len(containers)

#view html of nth product 
contain = containers[0]
container = containers[0]

#container.find("div","item-info").div

#filename = "products.csv"
#f = open(filename, "w")

#headers = "brand, product_name, price\n"

#f.write(headers)

for container in containers:

	# grabs product's company name

	###### ADD IF/ELSE FOR VALIDATION
	brand = container.find("div","item-info").div.a.img["title"]

	title_container = container.findAll("a",{"class":"item-title"})

	#grabs product name
	product_name = title_container[0].text

	str = container.findAll("li",{"class":"price-current"})[0].text



	str_nums = re.findall(r"[-+]?\d*\.\d+|\d+", str)

	#grabs product price
	product_price = str_nums[0]

	print("brand: " + brand) 
	print("product name: " + product_name)
	print("product price: " + product_price)

	# f.write(brand + "," + product_name.replace(",","|") + "," + product_price + "\n")


f.close()