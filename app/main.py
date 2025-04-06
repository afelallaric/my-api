
from fastapi import FastAPI
from datetime import datetime, timezone
import time

app = FastAPI()

start_time = time.time()  # Waktu saat server start


@app.get("/health")
def health_check():
    current_time = datetime.now(timezone.utc).isoformat()
    uptime_seconds = time.time() - start_time
    uptime_str = str(int(uptime_seconds)) + "s"

    return {
        "nama": "Rafi Budi Kinan",
        "nrp": "213576123497",
        "status": "UP",
        "timestamp": current_time,
        "uptime": uptime_str
    }
