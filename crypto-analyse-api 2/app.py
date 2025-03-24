
from flask import Flask, request, jsonify, render_template
from services.coingecko import get_price_and_history
from services.indicators import calculate_indicators
from services.gpt import generate_analysis

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/empfehlung", methods=["GET"])
def empfehlung():
    coin = request.args.get("coin", "bitcoin")
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
    app.run(debug=True)
