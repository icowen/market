# Market
Using [alphavantage](https://www.alphavantage.co/documentation/), this python file
can get data on stocks, crypto, and more.

## To begin:
1. Go to terminal and run `git clone https://github.com/icowen/market.git`.
2. `cd market`
3. `pip install -r requiremnets.txt`
4. Go to [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key)
    and create an api key.
5. Paste that api key on line 5 of `market.py`

        API_KEY = 'A893489MI013MIR1MQKADSD'
6. Run `python market.py`

## Next Steps
Read through the documentation [alphavantage](https://www.alphavantage.co/documentation/)
in order to discover what services are available.

- You can change the stock by updating `symbol = 'IBM'`
- You can change the interval of data collection by updating `interval = '5min'`
- You can change the what type of data is returned by updating `funcction = 'TIME_SERIES_INTRADAY'`
