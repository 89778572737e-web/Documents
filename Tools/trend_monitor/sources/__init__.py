"""
Источники данных радара. Каждый источник — отдельный файл («вилка в розетку»):
в нём функция fetch(config) -> list[dict], где у каждого кандидата поля:
  term (str)      — что растёт (поисковый запрос или название товара)
  growth_pct (float) — рост интереса в процентах
  source (str)    — имя источника
Чтобы добавить новый источник, достаточно положить файл сюда и вписать его имя в config.json.
"""
import importlib


def load(name):
    return importlib.import_module(f"sources.{name}")
