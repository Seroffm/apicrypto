
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_analysis(coin, preis, rsi, ma_7, ma_30):
    prompt = f"""
Du bist ein professioneller Krypto-Marktanalyst. Hier sind die aktuellen Daten für {coin}:

- Preis: {preis} USD
- RSI: {rsi}
- MA (7 Tage): {ma_7}
- MA (30 Tage): {ma_30}

Gib bitte eine Empfehlung ab (Kaufen, Halten oder Verkaufen) und eine kurze Begründung (1-2 Sätze).
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Du bist ein professioneller Krypto-Analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        content = response["choices"][0]["message"]["content"]
        zeilen = content.strip().split("\n")
        empfehlung = zeilen[0].split(":")[-1].strip()
        begruendung = zeilen[1] if len(zeilen) > 1 else ""

        return empfehlung, begruendung
    except Exception as e:
        return "Fehler", str(e)
