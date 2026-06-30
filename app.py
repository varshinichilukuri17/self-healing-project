from flask import Flask
import logging
from prometheus_client import Counter, generate_latest
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["http://localhost:9090", "http://127.0.0.1:9090", "http://54.160.176.172:9090"])

# Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Prometheus metric
REQUEST_COUNT = Counter("request_count", "Total Requests")

# Home route
@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Self-Healing DevOps Project Running"

# Health check route
@app.route('/health')
def health():
    REQUEST_COUNT.inc()
    return "Application is healthy"

# Error simulation route
@app.route('/error')
def error():
    REQUEST_COUNT.inc()
    try:
        raise Exception("Application error detected!")
    except Exception as e:
        logging.error(str(e))
        return "Root Cause Found: Application error detected!\nSelf-Healing Action Triggered!\nRestarting application..."

# Metrics route for Prometheus
@app.route('/metrics')
def metrics():
    return generate_latest()

# Main runner
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)