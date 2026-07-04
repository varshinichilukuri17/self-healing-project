from flask import Flask, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import psutil
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total number of requests'
)

start_time = time.time()

@app.route("/")
def home():
    REQUEST_COUNT.inc()

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = int(time.time() - start_time)

    return render_template(
        "index.html",
        cpu=cpu,
        memory=memory,
        disk=disk,
        uptime=uptime
    )

@app.route("/health")
def health():
    return "Application is healthy"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        'Content-Type': CONTENT_TYPE_LATEST
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)