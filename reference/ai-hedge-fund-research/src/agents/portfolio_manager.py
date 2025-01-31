from langchain_core.messages import AIMessage
import json

def portfolio_management_agent(state: dict):
    """Agent responsible for portfolio management and final decision making"""
    portfolio = state["data"]["portfolio"]
    risk_score = state["data"]["risk_score"]
    technical_indicators = state["data"]["technical_indicators"]
    fundamentals = state["data"]["fundamentals"]
    sentiment = state["data"]["sentiment"]
    
    # Generate trading decision based on analysis
    decision = generate_trading_decision(
        portfolio,
        risk_score,
        technical_indicators.iloc[-1],
        fundamentals,
        sentiment
    )
    
    # Create final decision message
    message = AIMessage(
        content=json.dumps(decision)
    )
    
    # Update state with final decision
    state["data"]["decision"] = decision
    state["messages"].append(message)
    
    return state

def generate_trading_decision(portfolio, risk_score, technical, fundamentals, sentiment):
    """Generate final trading decision based on all factors"""
    # Calculate position size based on risk score
    max_position = portfolio["portfolio_value"] * (1 - risk_score)
    
    # Determine action based on technical and fundamental analysis
    if technical['SMA_20'] > technical['SMA_50'] and fundamentals['profit_margin'] > 0.1:
        action = "buy"
        quantity = min(max_position // technical['close'], 1000)  # Limit to 1000 shares
    elif technical['SMA_20'] < technical['SMA_50'] or fundamentals['profit_margin'] < 0:
        action = "sell"
        quantity = min(portfolio["stock"], 1000)  # Limit to 1000 shares
    else:
        action = "hold"
        quantity = 0
    
    return {
        "action": action,
        "quantity": quantity,
        "reasoning": {
            "technical": f"20-day SMA: {technical['SMA_20']:.2f}, 50-day SMA: {technical['SMA_50']:.2f}",
            "fundamentals": f"Profit Margin: {fundamentals['profit_margin']:.2%}",
            "sentiment": f"Positive Score: {sentiment['positive_score']:.2f}"
        }
    }