from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from tools.api import get_price_data

def market_data_agent(state: dict):
    """Agent responsible for collecting and processing market data"""
    ticker = state["data"]["ticker"]
    start_date = state["data"]["start_date"]
    end_date = state["data"]["end_date"]
    
    # Get price data from API
    price_data = get_price_data(ticker, start_date, end_date)
    
    # Create message with market data summary
    message = AIMessage(
        content=f"Market data for {ticker} from {start_date} to {end_date}:\n"
                f"- Open: {price_data.iloc[0]['open']:.2f}\n"
                f"- Close: {price_data.iloc[-1]['close']:.2f}\n"
                f"- High: {price_data['high'].max():.2f}\n"
                f"- Low: {price_data['low'].min():.2f}\n"
                f"- Volume: {price_data['volume'].mean():.0f}"
    )
    
    # Update state with market data
    state["data"]["price_data"] = price_data
    state["messages"].append(message)
    
    return state