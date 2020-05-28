import morele
import xkom
import db
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

with open(config["main"]["input_file"]) as f:
    content = f.readlines()
content = [x.strip() for x in content]

def track(items):
    for url in items:
        result = ""
        if "x-kom" in url:
            info = xkom.get_info(url)
        else:
            pass
        if "morele" in url:
            info = morele.get_info(url)
        else:
            pass
        if info is None:
            result = "not done"
        else:
            inserted = db.add_product_info(info)
            if inserted:
                result = "done"
            else:
                result = "not done"
        print(result)

while True:
    track(content)
    print("Scraping and DB tasks completed. Now sleeping for", config["main"]["delay"], "seconds")
    time.sleep(int(config["main"]["delay"]))
