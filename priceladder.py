import requests
import json

url = "https://api.bybit.com/v2/public/orderBook/L2?symbol=ETHUSD"

response = requests.request("GET", url)
response_json = json.loads(response.text)
class PriceLadder:
    ladder_data = response_json['result']
    ladder_length = len(ladder_data)

    # Method to initialzie class variables
    # def __init__(self):
    #     pass

    def findMid(self) :
        topSide = self.ladder_data[0]['side']
        topsideSize = 0
        botsideSize = 0
        midtopPrice = 0
        midbotPrice = 0
        midPrice = 0
        for i in range(self.ladder_length):
            # Counting amount of buy and sells per side
            if (self.ladder_data[i]['side'] == 'Buy'):
                topsideSize+=1

            # elif (self.ladder_data[i]['side'] == 'Sell'):
            #     botsideSize+=1
        midtopPrice = float(self.ladder_data[topsideSize]['price'])
        midbotPrice = float(self.ladder_data[topsideSize+1]['price'])

        midPrice = float((midbotPrice + midtopPrice)/2)
        print(midPrice)

    # Prototype for the main method
    def jsonLadder(self):
        ladder_length = len(self.ladder_data)
        for i in range(ladder_length):
            print(self.ladder_data[i])

# main_ladder = PriceLadder()
# main_ladder.jsonLadder()
# main_ladder.findMid()