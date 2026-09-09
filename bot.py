import os
import requests

ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

def get_stock_price(symbol):
    url = "https://www.alphavantage.co/query"

    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol.upper(),
        "apikey": ALPHA_VANTAGE_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        quote = data.get("Global Quote", {})
        price = quote.get("05. price")

        if price:
            return f"سعر سهم {symbol.upper()} الحالي: {float(price):.2f} دولار"

        return f"لم أستطع جلب سعر {symbol.upper()} الآن."

    except Exception as e:
        return f"حدث خطأ أثناء جلب السعر: {e}"
