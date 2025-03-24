
def calculate_indicators(df):
    delta = df["preis"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    rsi_value = round(rsi.iloc[-1], 2)

    ma_7 = round(df["preis"].rolling(window=7).mean().iloc[-1], 2)
    ma_30 = round(df["preis"].rolling(window=30).mean().iloc[-1], 2)

    return rsi_value, ma_7, ma_30
