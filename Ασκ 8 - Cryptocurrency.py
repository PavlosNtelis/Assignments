import urllib.request
import json
from time import sleep
def get_coin_data(coin):
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    d=json.loads(html)
    return d[coin]["EUR"]

def euros(dict):
    print("BTC = ", btc, "€")
    print("ETH = ", eth, "€")
    print("LTC = ", ltc, "€")

print("Enter the file name with the .txt extension")
x = input()
with open(x) as f: 
    crypto = f.read() 
      
dict = json.loads(crypto)
btc = get_coin_data("BTC") * dict["BTC"]
eth = get_coin_data("ETH") * dict["ETH"]
ltc = get_coin_data("LTC") * dict["LTC"]
euros(dict)

#Δεν ξέρω αν θέλατε να τρέχει σε λούπα οπότε το αφήνω εδώ με σχόλιο

#for i in range(10):
#    dict = json.loads(crypto)
#    btc = get_coin_data("BTC") * dict["BTC"]
#    eth = get_coin_data("ETH") * dict["ETH"]
#    ltc = get_coin_data("LTC") * dict["LTC"]
#    euros(dict)
#    sleep(4)



