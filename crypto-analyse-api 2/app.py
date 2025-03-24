
from flask import Flask, request, jsonify, render_template
import os
from services.coingecko import get_price_and_history
from services.indicators import calculate_indicators
from services.gpt import generate_analysis

coin_aliases = {
    "btc": "bitcoin",
    "bitcoin": "bitcoin",
    "eth": "ethereum",
    "link": "chainlink",
    "chainlink": "chainlink",
    "bnb": "binancecoin",
    "xrp": "ripple",
    "ada": "cardano",
    "sol": "solana",
    "dot": "polkadot"
}

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/empfehlung", methods=["GET"])
def empfehlung():
    coin_input = request.args.get("coin", "bitcoin").lower()
    coin = coin_aliases.get(coin_input, coin_input)
    try:
        preis, history = get_price_and_history(coin)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    rsi, ma_7, ma_30 = calculate_indicators(history)
    empfehlung, begruendung = generate_analysis(coin, preis, rsi, ma_7, ma_30)

    return jsonify({
        "coin": coin,
        "preis": preis,
        "rsi": rsi,
        "ma_7": ma_7,
        "ma_30": ma_30,
        "empfehlung": empfehlung,
        "begründung": begruendung
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
