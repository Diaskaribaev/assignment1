from pycoingecko import CoinGeckoAPI
from rich import print
cg = CoinGeckoAPI()
top=input()
num=int(top)
total=cg.get_coins_markets(vs_currency='usd', per_page=num)

print(total)
