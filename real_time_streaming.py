import time
import random
from datetime import datetime

print("===== REAL-TIME DATA STREAMING =====")
print("Streaming started...\n")

while True:
    data = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "rainfall": round(random.uniform(0, 20), 2)
    }

    print(data)

    time.sleep(2)