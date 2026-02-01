import requests
import csv
import io
import os

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

message = "📊 **Message test**\n"

requests.post(DISCORD_WEBHOOK, json={"content": message})
