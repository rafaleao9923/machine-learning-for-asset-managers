import pandas as pd
import requests
import os
from datetime import datetime

def get_price_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Get historical price data for a ticker"""
    api_key = os.getenv('FINANCIAL_DATASETS_API_KEY')
    url = f"https://api.example.com/prices?ticker={ticker}&start_date={start_date}&end_date={end_date}&api_key={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    # Convert to DataFrame and parse dates
    df = pd.DataFrame(data['prices'])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    return df

def get_fundamentals_data(ticker: str) -> dict:
    """Get fundamental data for a ticker"""
    api_key = os.getenv('FINANCIAL_DATASETS_API_KEY')
    url = f"https://api.example.com/fundamentals?ticker={ticker}&api_key={api_key}"
    
    response = requests.get(url)
    return response.json()

def get_sentiment_data(ticker: str) -> dict:
    """Get sentiment data for a ticker"""
    api_key = os.getenv('FINANCIAL_DATASETS_API_KEY')
    url = f"https://api.example.com/sentiment?ticker={ticker}&api_key={api_key}"
    
    response = requests.get(url)
    return response.json()