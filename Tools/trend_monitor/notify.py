"""
Отправка сообщения в Telegram.

Токен бота берётся из секрета GitHub (TELEGRAM_BOT_TOKEN), в коде его нет.
Номер чата: из секрета TELEGRAM_CHAT_ID, если он задан; иначе из файла-памяти
Knowledge_Base/_Radar/chat_id.txt; иначе радар сам находит его по сообщению /start,
которое ты отправил боту (Telegram хранит такие сообщения около суток), и запоминает.
Номер чата в логи не печатается.
"""
import json
import os
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CHAT_FILE = os.path.join(HERE, "..", "..", "Knowledge_Base", "_Radar", "chat_id.txt")


def _api(token, method, payload=None):
    url = f"https://api.telegram.org/bot{token}/{method}"
    if payload is None:
        req = urllib.request.Request(url)
    else:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"),
                                     headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def find_chat_id(token):
    """Ищет номер личного чата по последнему сообщению, присланному боту."""
    data = _api(token, "getUpdates")
    for upd in reversed(data.get("result", [])):
        chat = (upd.get("message") or {}).get("chat") or {}
        if chat.get("type") == "private" and "id" in chat:
            return str(chat["id"])
    return None


def resolve_chat_id(token):
    chat = os.environ.get("TELEGRAM_CHAT_ID")
    if chat:
        return chat
    if os.path.exists(CHAT_FILE):
        saved = open(CHAT_FILE, encoding="utf-8").read().strip()
        if saved:
            return saved
    chat = find_chat_id(token)
    if chat:
        os.makedirs(os.path.dirname(CHAT_FILE), exist_ok=True)
        with open(CHAT_FILE, "w", encoding="utf-8") as f:
            f.write(chat)
        return chat
    raise RuntimeError("Не найден чат для отправки. Открой своего бота в Telegram и нажми Start, "
                       "потом запусти радар снова в течение суток.")


def send(text, dry_run=False):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if dry_run or not token:
        print("---- (Telegram не отправлялся: тестовый режим или нет токена) ----")
        print(text)
        print("---- конец сообщения ----")
        return False
    chat = resolve_chat_id(token)
    res = _api(token, "sendMessage", {"chat_id": chat, "text": text})
    return bool(res.get("ok"))
