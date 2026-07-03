import requests
import time
import os

APP_URL = "http://localhost:5000/health"

while True:
    try:
        response = requests.get(APP_URL)

        if response.status_code == 200:
            print("Application is healthy")

    except:
        print("Application is down! Restarting...")
        os.system("docker restart self-healing-app")

    time.sleep(10)