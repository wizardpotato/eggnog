import bs4
import requests
from bs4 import BeautifulSoup



def ticker():
    r=requests.get("https://www.livecoinwatch.com/price/Bitcoin-BTC")
    soup=bs4.BeautifulSoup(r.text,"xml")
    price=soup.find("span", {"class" : "price"}).text
    return price

while True:
    print("BTC/USDT: "+str(ticker()))
