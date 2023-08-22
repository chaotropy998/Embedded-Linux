# Writing a python code that fetches bitcoin rate
import requests

url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(url.json()['bpi']['USD'])