import healer

def analyze_logs():
    with open("app.log", "r") as file:
        logs = file.readlines()

    for log in logs:
        if "ERROR" in log:
            print("Root Cause Found: Application error detected!")
            healer.auto_heal()
            return

    print("System Healthy")

analyze_logs()