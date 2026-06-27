from flask import Flask
import logging
import healer

logging.basicConfig(filename="app.log", level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("Home page accessed")
    return "Self-Healing DevOps Project Running!"

@app.route("/health")
def health():
    app.logger.info("Health check accessed")
    return "Healthy"

@app.route("/error")
def error():
    app.logger.error("Simulated application error")
    return "Error occurred!", 500

@app.route("/metrics")
def metrics():
    return healer.get_metrics()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)