
import warnings
warnings.filterwarnings("ignore")

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the crew builder
from crew import financial_trading_crew

def run():
    """
    Runs the financial trading multi-agent system
    """

    inputs = {
        "stock_selection": "AAPL",
        "initial_capital": "100000",
        "risk_tolerance": "Medium",
        "trading_strategy_preference": "Day Trading",
        "news_impact_consideration": True
    }

    result = financial_trading_crew.kickoff(inputs=inputs)

    print("\n\n========== FINAL RESULT ==========\n")
    print(result)

if __name__ == "__main__":
    run()

