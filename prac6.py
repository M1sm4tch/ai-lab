class StockExpertSystem:
    def __init__(self):
        self.stock_data = {
            "AAPL": {"price": 150.50, "volume": 1000000, "trend": "up"},
            "GOOGL": {"price": 2800.75, "volume": 500000, "trend": "down"},
            "MSFT": {"price": 300.20, "volume": 800000, "trend": "up"}
            # Add more stocks with their data
        }

    def get_recommendation(self, symbol):
        stock = self.stock_data.get(symbol)
        if not stock:
            return "Stock not found"
        
        price = stock["price"]
        volume = stock["volume"]
        trend = stock["trend"]

        if price < 100:
            if volume > 500000:
                return "Buy"
            else:
                return "Hold"
        elif price > 200:
            if trend == "up":
                return "Sell"
            else:
                return "Hold"
        else:
            return "Hold"


# Example usage:
expert_system = StockExpertSystem()
symbol = input("Enter stock symbol (e.g., AAPL, GOOGL, MSFT): ").upper()
recommendation = expert_system.get_recommendation(symbol)
print("Recommendation for", symbol, ":", recommendation)
