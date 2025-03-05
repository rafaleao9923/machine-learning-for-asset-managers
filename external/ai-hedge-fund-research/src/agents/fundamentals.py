from langchain_core.messages import AIMessage
from tools.api import get_fundamentals_data

def fundamentals_agent(state: dict):
    """Agent responsible for fundamental analysis"""
    ticker = state["data"]["ticker"]
    
    # Get fundamentals data from API
    fundamentals = get_fundamentals_data(ticker)
    
    # Generate fundamentals analysis summary
    message = AIMessage(
        content=f"Fundamental Analysis for {ticker}:\n"
                f"- Market Cap: {fundamentals['market_cap'] / 1e9:.2f}B\n"
                f"- P/E Ratio: {fundamentals['pe_ratio']:.2f}\n"
                f"- Dividend Yield: {fundamentals['dividend_yield']:.2%}\n"
                f"- Revenue Growth: {fundamentals['revenue_growth']:.2%}\n"
                f"- Profit Margin: {fundamentals['profit_margin']:.2%}"
    )
    
    # Update state with fundamentals data
    state["data"]["fundamentals"] = fundamentals
    state["messages"].append(message)
    
    return state