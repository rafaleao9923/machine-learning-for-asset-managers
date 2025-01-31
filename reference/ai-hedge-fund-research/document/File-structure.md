# Project File Structure

```
ai-hedge-fund/
├── src/
│   ├── agents/                   # Agent definitions and workflow
│   │   ├── fundamentals.py       # Fundamental analysis agent
│   │   ├── market_data.py        # Market data agent
│   │   ├── portfolio_manager.py  # Portfolio management agent
│   │   ├── risk_manager.py       # Risk management agent
│   │   ├── sentiment.py          # Sentiment analysis agent
│   │   ├── state.py              # Agent state
│   │   ├── technicals.py         # Technical analysis agent
│   ├── tools/                    # Agent tools
│   │   ├── api.py                # API tools
│   ├── backtester.py             # Backtesting tools
│   ├── main.py                   # Main entry point
├── research/                     # Research documentation
├── pyproject.toml                # Dependency management
├── poetry.lock                   # Locked dependencies
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── LICENSE                       # Project license
├── README.md                     # Project documentation
└── App-flow.md                   # Application workflow
```

## Key Files and Their Roles

1. **src/agents/**
   - Contains all agent implementations
   - Each agent handles specific aspect of analysis or decision making

2. **src/tools/api.py**
   - Provides interface to financial data APIs
   - Handles data retrieval and preprocessing

3. **src/main.py**
   - Main entry point for the application
   - Coordinates agent workflow

4. **src/backtester.py**
   - Implements backtesting functionality
   - Simulates trading strategies

5. **pyproject.toml**
   - Manages project dependencies and configuration
   - Defines Poetry package settings

6. **README.md**
   - Provides project overview and setup instructions
   - Includes usage examples and documentation

7. **App-flow.md**
   - Documents application workflow and architecture
   - Explains data flow and system components