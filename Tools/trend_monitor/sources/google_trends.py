"""
Источник: Google Trends, «растущие запросы» (rising) по всему миру.
Используется неофициальная библиотека pytrends. Она может ломаться или получать
отказ от Google при частых запросах — поэтому между запросами есть пауза,
а любая ошибка не скрывается, а возвращается в отчёт (см. run.py).
"""
import time


def fetch(config):
    from pytrends.request import TrendReq

    pt = TrendReq(hl="en-US", tz=0, timeout=(10, 25))
    found, errors = [], []
    for term in config["seed_terms"]:
        try:
            pt.build_payload([term], timeframe=config["timeframe"], geo=config["geo"],
                             cat=config.get("category", 0))
            rising = pt.related_queries().get(term, {}).get("rising")
            if rising is not None:
                stop = [w.lower() for w in config.get("stop_words", [])]
                for _, row in rising.iterrows():
                    q = str(row["query"]).lower()
                    if any(w in q for w in stop):
                        continue
                    found.append({
                        "term": str(row["query"]),
                        "growth_pct": float(row["value"]),
                        "source": "google_trends",
                        "seed": term,
                    })
        except Exception as e:  # один сбойный запрос не должен ронять весь радар
            errors.append(f"{term}: {type(e).__name__}: {str(e)[:120]}")
        time.sleep(config.get("pause_between_requests_sec", 8))
    if errors and not found:
        raise RuntimeError("Google Trends не вернул данных. " + " | ".join(errors[:3]))
    return found
