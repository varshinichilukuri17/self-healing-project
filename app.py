from flask import Flask
import logging

app = Flask(__name__)

# Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Home route
@app.route('/')
def home():
    return "Self-Healing DevOps Project Running"

# Health check route
@app.route('/health')
def health():
    return "Application is healthy"

# Error simulation route
@app.route('/error')
def error():
    try:
        raise Exception("Application error detected!")
    except Exception as e:
        logging.error(str(e))
        return "Root Cause Found: Application error detected!\nSelf-Healing Action Triggered!\nRestarting application..."

# Main runner
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)