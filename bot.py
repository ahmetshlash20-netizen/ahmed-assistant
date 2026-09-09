import os
import requests

ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

def get_stock_price(symbol):
    try:
        url = "https://www.alphavantage.co/query"

        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol.upper(),
            "apikey": ALPHA_VANTAGE_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()

        quote = data.get("Global Quote", {})
        price = quote.get("05. price")

        if price:
            return f"السعر الحالي لسهم {symbol.upper()} هو {price} دولار"

        return f"لم أستطع جلب سعر {symbol.upper()}"

    except Exception as e:
        return f"حدث خطأ أثناء جلب السعر: {e}"

APL")print (get_stock_price("AAPL"))
