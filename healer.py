import os
import requests
import time

def check_health():
    try:
        response = requests.get("http://localhost:5000/health")
        if response.status_code == 200:
            print("Application is healthy")
        else:
            print("Application unhealthy. Restarting...")
            restart_container()
    except:
        print("Application down. Restarting...")
        restart_container()

def restart_container():
    os.system("docker restart self-healing-container")
    print("Container restarted")

while True:
    check_health()
    time.sleep(10)