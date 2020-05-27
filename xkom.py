import requests
from bs4 import BeautifulSoup as soup

def get_info(url):
    try:
        info = {"name": "", "price": 0, "url": "", "vendor": ""}
        page_html = requests.get(url)
        page_soup = soup(page_html.text, "html.parser")
        info["name"] = page_soup.findAll("h1")[0].text.strip()
        info["price"] = page_soup.findAll("div",{"class":"u7xnnm-4 iVazGO"})[0].text.replace(",",".").replace("zł","").replace(" ","")
        info["url"] = url
        info["vendor"] = "xkom"
        return info
    except Exception as identifier:
        print("[FATAL ERROR] X-KOM")
        print(identifier)
        info = None
        pass
