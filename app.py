from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter("request_count", "Total Requests")


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Self-Healing DevOps Project Running"


@app.route("/health")
def health():
    REQUEST_COUNT.inc()
    return "Application is healthy"


@app.route("/error")
def error():
    REQUEST_COUNT.inc()
    return """
    Root Cause Found: Application error detected!
    Self-Healing Action Triggered! Restarting application...
    """


@app.route("/metrics")
def metrics():
    return generate_latest()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)