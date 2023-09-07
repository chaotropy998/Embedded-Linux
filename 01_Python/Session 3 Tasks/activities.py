import requests
from time import sleep
while True:
    url = requests.get("https://www.boredapi.com/api/activity")
    print("Here's a suggested activity for you: " + url.json()['activity'])
    sleep(3)