from langchain_core.messages import AIMessage
from tools.api import get_sentiment_data

def sentiment_agent(state: dict):
    """Agent responsible for sentiment analysis"""
    ticker = state["data"]["ticker"]
    
    # Get sentiment data from API
    sentiment = get_sentiment_data(ticker)
    
    # Generate sentiment analysis summary
    message = AIMessage(
        content=f"Sentiment Analysis for {ticker}:\n"
                f"- Overall Sentiment: {sentiment['overall_sentiment']}\n"
                f"- Positive Score: {sentiment['positive_score']:.2f}\n"
                f"- Negative Score: {sentiment['negative_score']:.2f}\n"
                f"- Neutral Score: {sentiment['neutral_score']:.2f}"
    )
    
    # Update state with sentiment data
    state["data"]["sentiment"] = sentiment
    state["messages"].append(message)
    
    return state