import requests

API_KEY = 'PUT YOUR API KEY HERE'  # Put your api key here


def main():
    # For more options look at: https://www.alphavantage.co/documentation/

    # Change these to get different data
    function = 'TIME_SERIES_INTRADAY'
    interval = '5min'  # 1, 5, 15, 30, or 60
    symbol = 'IBM'

    # This is the endpoint you are actually hitting
    download = requests.get(
        f"https://www.alphavantage.co/query?"
        f"function={function}&"
        f"symbol={symbol}&"
        f"interval={interval}&"
        f"apikey={API_KEY}")
    print(f'download: {download}')

    data = download.content.decode('utf-8')
    print(f'data: {data}')
    # Do stuff with data here...


if __name__ == '__main__':
    main()
