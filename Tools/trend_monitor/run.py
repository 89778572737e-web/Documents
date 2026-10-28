"""
Радар трендов: раз в сутки собирает растущие запросы, убирает уже виденные
и присылает короткий список в Telegram.

ВАЖНО: радар находит ПОДСКАЗКИ (что растёт в поиске), а не проверенные товары.
Проверка поставщика, маржи и спроса остаётся за системой и за решением человека.
Радар никогда ничего не покупает и не тратит деньги.

Запуск:
    python3 Tools/trend_monitor/run.py              # боевой режим
    python3 Tools/trend_monitor/run.py --dry-run    # без отправки и без записи
    python3 Tools/trend_monitor/run.py --sample     # тестовые данные, без интернета
"""
import argparse
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import notify  # noqa: E402
import sources  # noqa: E402

REPO_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
STATE = os.path.join(REPO_ROOT, "Knowledge_Base", "_Radar", "seen.json")


def load_state():
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(state):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1, sort_keys=True)


def pick(candidates, seen, min_growth, limit):
    """Оставляет новые кандидаты с достаточным ростом, без повторов, по убыванию роста."""
    best = {}
    for c in candidates:
        key = c["term"].strip().lower()
        if key in seen or c["growth_pct"] < min_growth:
            continue
        if key not in best or c["growth_pct"] > best[key]["growth_pct"]:
            best[key] = c
    return sorted(best.values(), key=lambda c: -c["growth_pct"])[:limit]


def format_message(picked, today):
    lines = [f"Радар трендов, {today}", "",
             "Что растёт в поиске по всему миру за последнюю неделю.",
             "Это подсказки, а не проверенные товары. Покупать ничего не нужно.", ""]
    for i, c in enumerate(picked, 1):
        g = "резкий рост" if c["growth_pct"] >= 5000 else f"+{int(c['growth_pct'])}%"
        lines.append(f"{i}. {c['term']} ({g}, тема: {c.get('seed', '-')})")
    lines += ["", "Если что-то заинтересовало, напиши в Claude: проверю поставщика и маржу."]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--sample", action="store_true")
    args = ap.parse_args()

    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as f:
        config = json.load(f)
    if args.sample:
        config["sources"] = ["sample"]

    today = datetime.date.today().isoformat()
    candidates, problems = [], []
    for name in config["sources"]:
        try:
            candidates += sources.load(name).fetch(config)
        except Exception as e:
            problems.append(f"{name}: {type(e).__name__}: {str(e)[:300]}")

    if problems and not candidates:
        # Тишина не должна выглядеть как «трендов нет»: сообщаем о поломке.
        notify.send("Радар трендов не смог получить данные.\n" + "\n".join(problems)
                    + "\n\nЭто сбой источника, а не отсутствие трендов.", dry_run=args.dry_run)
        return 1

    state = load_state()
    picked = pick(candidates, state, config["min_growth_pct"], config["max_per_day"])

    if picked:
        notify.send(format_message(picked, today), dry_run=args.dry_run)
        if not args.dry_run:
            for c in picked:
                state[c["term"].strip().lower()] = today
            save_state(state)
    else:
        print(f"{today}: новых растущих запросов выше порога нет.")
    if problems:
        print("Часть источников сбоила:", *problems, sep="\n  ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
