# Application Flow Overview

## Main Components

1. **API Layer (src/tools/api.py)**
   - Provides financial data access through Financial Datasets API
   - Key functions:
     - `get_financial_metrics()` - Fetch financial metrics
     - `search_line_items()` - Search specific financial line items
     - `get_insider_trades()` - Get insider trading data
     - `get_market_cap()` - Retrieve company market capitalization
     - `get_prices()` - Fetch historical price data
     - `prices_to_df()` - Convert price data to DataFrame
     - `get_price_data()` - Get price data as DataFrame

2. **Core Logic (src/main.py)**
   - Implements hedge fund trading system using LangGraph
   - Agents:
     - Market Data Agent
     - Technical Analyst Agent
     - Fundamentals Agent
     - Sentiment Agent
     - Risk Management Agent
     - Portfolio Management Agent
   - Workflow:
     1. Market Data Agent collects initial data
     2. Data flows to Technical, Fundamentals, and Sentiment Agents
     3. All analysis converges to Risk Management Agent
     4. Risk assessment goes to Portfolio Management Agent
     5. Final decision is made

3. **Backtesting (src/backtester.py)**
   - Backtester class for strategy evaluation
   - Key features:
     - Portfolio tracking (cash, stock positions)
     - Trade execution with validation
     - Performance metrics calculation:
       - Total return
       - Sharpe ratio
       - Maximum drawdown
     - Portfolio value visualization

## Execution Flow

1. **Main Execution**
   - Run via `python src/main.py` with required parameters
   - Processes:
     - Parse command line arguments
     - Validate dates
     - Initialize portfolio
     - Run hedge fund workflow
     - Output final decision

2. **Backtesting Execution**
   - Run via `python src/backtester.py` with parameters
   - Processes:
     - Initialize backtester with agent and parameters
     - Simulate trading over date range
     - Execute trades based on agent decisions
     - Track portfolio value
     - Analyze and visualize performance

## Data Flow

1. API Layer fetches raw financial data
2. Data is processed and analyzed by agents
3. Risk assessment informs portfolio decisions
4. Backtester simulates strategy execution
5. Performance metrics are calculated and visualized
