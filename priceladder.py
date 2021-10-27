import requests
import json
import time

url = "https://api.bybit.com/v2/public/orderBook/L2?symbol=ETHUSD"

response = requests.request("GET", url)
response_json = json.loads(response.text)

class PriceLadder:
    ladder_data = response_json['result']

    def __init__(self):
        pass

    def findMid(self) :
        pass

    # Prototype for the main method
    def jsonLadder(self):
        ladder_length = len(self.ladder_data)
        for i in range(ladder_length):
            print(self.ladder_data[i])

main_ladder = PriceLadder()
main_ladder.jsonLadder()