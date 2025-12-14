import time
# Importar archivo del cliente S3
from s3_client import update_json_s3

def handle_event(event):
    update_json_s3(event)

handle_event({
    "event_type": "user_signup",
    "user_id": 12345,
    "timestamp": int(time.time())
})