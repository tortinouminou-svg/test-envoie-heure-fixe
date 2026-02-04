import requests
import csv
import io
import os
from datetime import datetime
from zoneinfo import ZoneInfo

ALLOWED_HOURS = {0, 4, 8, 12, 16, 20}

now_fr = datetime.now(ZoneInfo("Europe/Paris"))

if now_fr.minute != 5 or now_fr.hour not in ALLOWED_HOURS:
    print("⏭️ Pas le bon créneau")
    exit(0)

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

message = "📊 **Message test**\n"

requests.post(DISCORD_WEBHOOK, json={"content": message})
