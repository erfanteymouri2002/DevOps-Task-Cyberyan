from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest
import random

app = Flask(__name__)

crawler_fetch_total = Counter('crawler_fetch_total', 'Total fetch attempts')
crawler_success_total = Counter('crawler_success_total', 'Successful fetches')
crawler_error_total = Counter('crawler_error_total', 'Failed fetches')

@app.route("/fetch")
def fetch():
    crawler_fetch_total.inc()
    if random.choice([True, False]):
        crawler_success_total.inc()
        return jsonify({"status": "success"})
    else:
        crawler_error_total.inc()
        return jsonify({"status": "error"}), 500

@app.route("/metrics")
def metrics():
    return generate_latest(), 200

@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

