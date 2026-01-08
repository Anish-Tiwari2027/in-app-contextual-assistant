import json
import random

with open("data/reply_config.json", "r", encoding="utf-8") as f:
    REPLIES = json.load(f)

def get_reply(intent):
    if intent in REPLIES:
        return random.choice(REPLIES[intent])
    return random.choice(REPLIES["fallback"])
