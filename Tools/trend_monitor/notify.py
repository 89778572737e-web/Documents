"""Отправка сообщения в Telegram. Токен и номер чата берутся из переменных окружения (секреты GitHub), в коде их нет."""
import json
import os
import urllib.request


def send(text, dry_run=False):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat = os.environ.get("TELEGRAM_CHAT_ID")
    if dry_run or not token or not chat:
        print("---- (Telegram не отправлялся: тестовый режим или нет настроек) ----")
        print(text)
        print("---- конец сообщения ----")
        return False
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=json.dumps({"chat_id": chat, "text": text}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status == 200
