import requests
import time
import os
from datetime import datetime

APP_URL = "http://localhost:5000/health"

while True:
    try:
        response = requests.get(APP_URL)

        if response.status_code == 200:
            print("Application is healthy")

    except:
        print("Application is down! Restarting...")

        with open("recovery.log", "a") as log:
            log.write(
                f"[{datetime.now()}] Application failed. Restarting container...\n"
            )

        os.system("docker restart self-healing-app")

        with open("recovery.log", "a") as log:
            log.write(
                f"[{datetime.now()}] Container restarted successfully.\n"
            )

    time.sleep(10)