import requests
import time

ALPHA_VANTAGE_KEY = "2M7L6W7XVL0EWXC0"
AV_BASE_URL = "https://www.alphavantage.co/query"

class HunterAgent:
    def __init__(self, goal="Find investment opportunities"):
        self.goal = goal
        self.api_key = ALPHA_VANTAGE_KEY
        self.opportunities = []
        print("=" * 60)
        print("Hunter Agent V3.0 Initialized!")
        print("=" * 60)
        print(f"Goal: {self.goal}")
        print("=" * 60)
    
    def get_stock_data(self, symbol):
        url = f"{AV_BASE_URL}?function=OVERVIEW&symbol={symbol}&apikey={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            if data.get("Symbol"):
                return {
                    "symbol": symbol,
                    "name": data.get("Name", "Unknown"),
                    "sector": data.get("Sector", "Unknown"),
                    "pe_ratio": float(data.get("PERatio", 0) or 0),
                    "profit_margin": float(data.get("ProfitMargin", 0) or 0) * 100
                }
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def discover(self, symbols):
        print(f"\nDiscovering opportunities in {len(symbols)} stocks...\n")
        
        for symbol in symbols:
            print(f"Analyzing {symbol}...")
            data = self.get_stock_data(symbol)
            
            if data:
                print(f"  Name: {data['name']}")
                print(f"  Sector: {data['sector']}")
                print(f"  P/E Ratio: {data['pe_ratio']:.2f}")
                print(f"  Profit Margin: {data['profit_margin']:.2f}%")
                print()
                self.opportunities.append(data)
            
            time.sleep(12)
        
        print("=" * 60)
        print(f"Discovery Complete! Found {len(self.opportunities)} opportunities")
        print("=" * 60)
        return self.opportunities

if __name__ == "__main__":
    agent = HunterAgent()
    stocks = ["AAPL", "GOOGL", "MSFT"]
    opportunities = agent.discover(stocks)
