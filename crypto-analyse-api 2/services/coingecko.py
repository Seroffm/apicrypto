
import requests
import pandas as pd

def get_price_and_history(coin):
    url_price = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    url_history = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=30"

    price_res = requests.get(url_price).json()
    history_res = requests.get(url_history).json()

    preis = price_res[coin]['usd']
    df = pd.DataFrame(history_res["prices"], columns=["timestamp", "preis"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
    df.set_index("timestamp", inplace=True)

    return preis, df
