import requests
from time import sleep

x = requests.get('https://www.varzesh3.com/')

while True:
    y = requests.get('https://www.varzesh3.com/')
    # print(y.text)
    if x.text == y.text:
        print(True)
    else:
        print(False)
    x = y
    sleep(3)
