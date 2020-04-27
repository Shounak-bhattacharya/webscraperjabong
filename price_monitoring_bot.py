import requests
from bs4 import BeautifulSoup
url="https://www.jabong.com/find/denims?tt=denims&rank=0"
response=requests.get(url)
soup= BeautifulSoup(response.text,'html.parser')
main_body=soup.find('section',class_='row search-product animate-products')
all_denims=main_body.find_all('div',class_='col-xxs-6 col-xs-4 col-sm-4 col-md-3 col-lg-3 product-tile img-responsive')
for denim in all_denims:
     denim_name=denim.find('div', class_='h4')
     denim_price=denim.find('div', class_='price')
     print(denim_name.text)
     print(denim_price.text)
     if (float(denim_price.text))<= 2000:
        print('within your budget',denim_name.text,"     :    ",denim_price.text)
