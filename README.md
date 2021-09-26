# CoinGecko API wrapper

### Installation
PyPi 
```bash
pip install pycoingecko
```

or from source

```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

### Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

### Examples
```python
# firstly input number 'x' which will show top 'x' cryptocurencies
>>>top=input()
>>>num=int(top)
# /coins/markets List all supported coins price, market cap, volume, and market related data
>>>cg.get_coins_markets(vs_currency='usd', per_page=num)
    {
        'id': 'bitcoin',
        'symbol': 'btc',
        'name': 'Bitcoin',
        'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579',
        'current_price': 43295,
        'market_cap': 816994647734,
        'market_cap_rank': 1,
        'fully_diluted_valuation': 911304655196,
        'total_volume': 32141113207,
        'high_24h': 44229,
        'low_24h': 40890,
        'price_change_24h': 679.48,
        'price_change_percentage_24h': 1.59444,
        'market_cap_change_24h': 17314877086,
        'market_cap_change_percentage_24h': 2.16523,
        'circulating_supply': 18826731.0,
        'total_supply': 21000000.0,
        'max_supply': 21000000.0,
        'ath': 64805,
        'ath_change_percentage': -33.18963,
        'ath_date': '2021-04-14T11:54:46.763Z',
        'atl': 67.81,
        'atl_change_percentage': 63750.33251,
        'atl_date': '2013-07-06T00:00:00.000Z',
        'roi': None,
        'last_updated': '2021-09-26T13:40:37.892Z'
    },
    {
        'id': 'ethereum',
        'symbol': 'eth',
        'name': 'Ethereum',
        'image': 'https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880',
        'current_price': 2999.78,
        'market_cap': 353711519540,
        'market_cap_rank': 2,
        'fully_diluted_valuation': None,
        'total_volume': 26275641973,
        'high_24h': 3056.55,
        'low_24h': 2745.41,
        'price_change_24h': 78.99,
        'price_change_percentage_24h': 2.70426,
        'market_cap_change_24h': 11293505385,
        'market_cap_change_percentage_24h': 3.29816,
        'circulating_supply': 117682510.374,
        'total_supply': None,
        'max_supply': None,
        'ath': 4356.99,
        'ath_change_percentage': -31.15003,
        'ath_date': '2021-05-12T14:41:48.623Z',
        'atl': 0.432979,
        'atl_change_percentage': 692725.20403,
        'atl_date': '2015-10-20T00:00:00.000Z',
        'roi': {'times': 91.51924025116644, 'currency': 'btc', 'percentage': 9151.924025116645},
        'last_updated': '2021-09-26T13:39:44.615Z'
    },
    {
        'id': 'cardano',
        'symbol': 'ada',
        'name': 'Cardano',
        'image': 'https://assets.coingecko.com/coins/images/975/large/cardano.png?1547034860',
        'current_price': 2.27,
        'market_cap': 72831186569,
        'market_cap_rank': 3,
        'fully_diluted_valuation': 102206806794,
        'total_volume': 4437616416,
        'high_24h': 2.45,
        'low_24h': 2.15,
        'price_change_24h': -0.106505772935,
        'price_change_percentage_24h': -4.48792,
        'market_cap_change_24h': -3244950380.1595306,
        'market_cap_change_percentage_24h': -4.2654,
        'circulating_supply': 32066390668.4135,
        'total_supply': 45000000000.0,
        'max_supply': 45000000000.0,
        'ath': 3.09,
        'ath_change_percentage': -26.57376,
        'ath_date': '2021-09-02T06:00:10.474Z',
        'atl': 0.01925275,
        'atl_change_percentage': 11672.88035,
        'atl_date': '2020-03-13T02:22:55.044Z',
        'roi': None,
        'last_updated': '2021-09-26T13:40:36.973Z'
    }



```




## License
[MIT](https://choosealicense.com/licenses/mit/)
