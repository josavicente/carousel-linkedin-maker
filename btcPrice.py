import requests 
import rumps

class AwesomeStatusBarApp(rumps.App) :
    
    def __init__ (self):
        super(AwesomeStatusBarApp, self).__init__("BettaTech")
        self.menu = ["Querying API..."]
    
    @rumps.timer(1)
    
    def sayhi(self, _):
        headers = {
            'Content-Type' : 'application/json',
        }
        r = requests. get ("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
        print(r.json()['data']['rates']['EUR'])
        self.title = r.json () ['data'] ['rates'] ['EUR']
if __name__ == "__main__":
    AwesomeStatusBarApp().run()