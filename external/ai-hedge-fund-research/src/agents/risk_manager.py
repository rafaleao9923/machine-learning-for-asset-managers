from langchain_core.messages import AIMessage

def risk_management_agent(state: dict):
    """Agent responsible for risk management"""
    portfolio = state["data"]["portfolio"]
    technical_indicators = state["data"]["technical_indicators"]
    fundamentals = state["data"]["fundamentals"]
    sentiment = state["data"]["sentiment"]
    
    # Calculate risk score based on various factors
    risk_score = calculate_risk_score(
        technical_indicators.iloc[-1],
        fundamentals,
        sentiment
    )
    
    # Generate risk assessment message
    message = AIMessage(
        content=f"Risk Assessment:\n"
                f"- Overall Risk Score: {risk_score:.2f}\n"
                f"- Portfolio Value: ${portfolio['portfolio_value']:,.2f}\n"
                f"- Recommended Action: {'Reduce Exposure' if risk_score > 0.7 else 'Maintain Position'}"
    )
    
    # Update state with risk assessment
    state["data"]["risk_score"] = risk_score
    state["messages"].append(message)
    
    return state

def calculate_risk_score(technical, fundamentals, sentiment):
    """Calculate comprehensive risk score"""
    # Technical risk factors
    tech_risk = 0.4 * (1 - technical['RSI']/100) + 0.6 * (technical['SMA_20'] < technical['SMA_50'])
    
    # Fundamental risk factors
    fund_risk = 0.3 * (1 - fundamentals['profit_margin']) + 0.7 * (fundamentals['pe_ratio'] > 20)
    
    # Sentiment risk factors
    sent_risk = 0.5 * (1 - sentiment['positive_score']) + 0.5 * sentiment['negative_score']
    
    # Weighted average of all risk factors
    return 0.4 * tech_risk + 0.4 * fund_risk + 0.2 * sent_risk