from flask import Flask, jsonify, render_template
import requests
import os

API_BASE_URL = "http://quote-api:8000"
WEBAPP_PORT = os.getenv("WEBAPP_PORT", "5000")

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def get_quote():
    try:
        response = requests.get(f"{API_BASE_URL}")
        # Raise HTTPError is request return unsuccessful status
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"HTTP error occured: {http_err}"}), 500
    except Exception as err:
        return jsonify({"error": f"Other error occured: {err}"}), 500
    return render_template("index.html", quote=data["quote"], author=data["author"])


@app.route("/howmany")
def get_quotes_count():
    try:
        response = requests.get("http://192.168.64.2:8000/howmany")
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"HTTP error occured: {http_err}"}), 500
    except Exception as err:
        return jsonify({"error": f"Other error occurent: {err}"}), 500
    return render_template("howmany.html", count_quote=data["nbQuotes"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(WEBAPP_PORT))
