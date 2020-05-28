from datetime import datetime
from influxdb import InfluxDBClient
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

def add_product_info(info):
    now = datetime.utcnow().replace(microsecond=0).isoformat("T") + "Z"
    json_body = [
        {
            "measurement": "price",
            "tags": {
                "vendor": info['vendor'],
                "item": info['name'],
                "url": info['url']
            },
            "time": now,
            "fields": {
                "value": float(info["price"])
            }
        }
    ]

    try:
        client = InfluxDBClient(config["db"]["address"], config["db"]["port"], config["db"]["user"], config["db"]["password"], config["db"]["db_name"])
        client.create_database(config["db"]["db_name"])
        print(json_body)
        client.write_points(json_body)
        # result = client.query('select value from price;')
        # print("Result: {0}".format(result))
        return True
    except Exception as identifier:
        print(identifier)
        return False
