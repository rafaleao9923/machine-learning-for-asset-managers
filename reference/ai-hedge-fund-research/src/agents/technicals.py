from langchain_core.messages import AIMessage
import pandas as pd
import numpy as np

def technical_analyst_agent(state: dict):
    """Agent responsible for technical analysis"""
    price_data = state["data"]["price_data"]
    
    # Calculate technical indicators
    price_data['SMA_20'] = price_data['close'].rolling(window=20).mean()
    price_data['SMA_50'] = price_data['close'].rolling(window=50).mean()
    price_data['RSI'] = calculate_rsi(price_data['close'])
    
    # Generate technical analysis summary
    latest_data = price_data.iloc[-1]
    message = AIMessage(
        content=f"Technical Analysis:\n"
                f"- 20-day SMA: {latest_data['SMA_20']:.2f}\n"
                f"- 50-day SMA: {latest_data['SMA_50']:.2f}\n"
                f"- RSI: {latest_data['RSI']:.2f}\n"
                f"- Current Trend: {'Bullish' if latest_data['SMA_20'] > latest_data['SMA_50'] else 'Bearish'}"
    )
    
    # Update state with technical data
    state["data"]["technical_indicators"] = price_data[['SMA_20', 'SMA_50', 'RSI']]
    state["messages"].append(message)
    
    return state

def calculate_rsi(prices, period=14):
    """Calculate Relative Strength Index (RSI)"""
    delta = prices.diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    
    avg_gain = pd.Series(gain).rolling(window=period).mean()
    avg_loss = pd.Series(loss).rolling(window=period).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi