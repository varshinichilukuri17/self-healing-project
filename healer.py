import os
import requests
import time
import healer

restart_count = 0
error_count = 0

def check_health():
    global error_count
    try:
        response = requests.get("http://localhost:5000/health")

        if response.status_code == 200:
            print("Application is healthy")
        else:
            print("Application unhealthy. Restarting...")
            error_count += 1
            restart_container()

    except Exception:
        print("Application down. Restarting...")
        error_count += 1
        restart_container()

def restart_container():
    global restart_count
    os.system("docker restart self-healing-container")
    restart_count += 1
    print(f"Container restarted. Total restarts: {restart_count}")

def get_metrics():
    return {
        "restart_count": restart_count,
        "error_count": error_count
    }

 @app.route("/metrics")
def metrics():
    return healer.get_metrics()

if __name__ == "__main__":
    while True:
        check_health()
        time.sleep(10)