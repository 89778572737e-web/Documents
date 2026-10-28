"""Тестовый источник: фиктивные данные для проверки движка без интернета. НЕ использовать в работе."""


def fetch(config):
    return [
        {"term": "TEST magnetic mini fan", "growth_pct": 4500, "source": "sample", "seed": "test"},
        {"term": "TEST pet water fountain", "growth_pct": 900, "source": "sample", "seed": "test"},
        {"term": "TEST usb desk lamp", "growth_pct": 150, "source": "sample", "seed": "test"},
        {"term": "TEST old repeat item", "growth_pct": 2000, "source": "sample", "seed": "test"},
    ]
