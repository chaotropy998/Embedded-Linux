import requests
url = requests.get("https://ipinfo.io/")
print("Your current IP address is: " + url.json()['ip'], end="\n")
print("Your current location is: " + url.json()['city'], end=" ")
print("in " + url.json()['country'])

