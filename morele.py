import requests
from bs4 import BeautifulSoup as soup

def get_info(url):
    try:
        info = {"name": "", "price": 0, "url": "", "vendor": ""}
        page_html = requests.get(url)
        page_soup = soup(page_html.text, "html.parser")
        info["name"] = page_soup.findAll("h1",{"class":"prod-name"})[0].text.replace("Karta graficzna","").strip()
        info["price"] = page_soup.find(id="product_price_brutto").text.replace(",",".").replace("zł","").replace(" ","")
        info["url"] = url
        info["vendor"] = "morele"
        return info
    except Exception as identifier:
        print("[FATAL ERROR] MORELE")
        print(identifier)
        info = None
        pass
