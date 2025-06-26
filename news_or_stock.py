import os
import requests
from dotenv import load_dotenv
from datetime import datetime

def log_action(action, status):
    with open('logs.txt', 'a') as log:
        log.write(f"{datetime.now()} | {action} | {status}\n")

def fetch_news():
    load_dotenv()
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        print('NEWS_API_KEY not found in .env')
        log_action('Fetch News', 'Failed: No API Key')
        return
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey=' + api_key
    try:
        resp = requests.get(url)
        data = resp.json()
        if data.get('status') != 'ok':
            print('Failed to fetch news:', data.get('message'))
            log_action('Fetch News', f"Failed: {data.get('message')}")
            return
        print('\nTop 3 US Business Headlines:')
        for i, article in enumerate(data['articles'], 1):
            print(f"{i}. {article['title']}")
        log_action('Fetch News', 'Success')
    except Exception as e:
        print('Error:', e)
        log_action('Fetch News', f'Failed: {e}')

def fetch_stock():
    load_dotenv()
    api_key = os.getenv('STOCK_API_KEY')
    if not api_key:
        print('STOCK_API_KEY not found in .env')
        log_action('Fetch Stock', 'Failed: No API Key')
        return
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}'
    try:
        resp = requests.get(url)
        data = resp.json()
        times = data.get('Time Series (5min)')
        if not times:
            print('Failed to fetch stock data:', data.get('Note', data))
            log_action('Fetch Stock', f"Failed: {data.get('Note', data)}")
            return
        latest = sorted(times.keys())[-1]
        open_price = times[latest]['1. open']
        print(f"IBM Stock (5min interval):\nTime: {latest}\nOpen Price: ${open_price}")
        log_action('Fetch Stock', 'Success')
    except Exception as e:
        print('Error:', e)
        log_action('Fetch Stock', f'Failed: {e}')

def news_or_stock_menu():
    print('\n1. View top 3 US business headlines')
    print('2. View IBM 5-min stock price')
    choice = input('Choose an option (1 or 2): ')
    if choice == '1':
        fetch_news()
    elif choice == '2':
        fetch_stock()
    else:
        print('Invalid choice.')
