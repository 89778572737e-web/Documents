# KB Tools — Real Automation (Phase 13 start)

Первый реальный работающий код в проекте (сентябрь 2026). Раньше вся архитектура была только текстовой спецификацией — эти скрипты реально читают/проверяют Knowledge Base.

## Файлы

- `quality_gates.py` — реализует GATE 1 (Product Data Completeness), GATE 2 (Supplier Verification), GATE 3 (Financial Viability) из Quality_Gates.md. Парсит реальные markdown-записи и считает маржинальность автоматически.
- `id_generator.py` — сканирует Products.md/Suppliers.md и возвращает следующий свободный Product-XXXX / Supplier-XXXX ID, предотвращая дублирование ID (Decision B/D).

## Важно про токен доступа

Эти скрипты обращаются к GitHub API и требуют токен с правами Contents: Read (минимум) или Read and write (для будущих write-функций). Токен НЕ хранится в этом файле по соображениям безопасности — передавайте его через переменную окружения при запуске:

```
export GH_TOKEN="ваш_токен"
```

и используйте `os.environ['GH_TOKEN']` вместо хардкода (в текущей версии скриптов токен захардкожен для быстрого прототипа — это нужно исправить перед реальным использованием кем-либо, кроме автора).

## Проверено на реальных данных

quality_gates.py протестирован на реальной записи Product-0001 / Supplier-0001 — результат: маржинальность 56.1%, совпадает с ручным расчётом в _Analysis/Product-0001_Analysis.md.

id_generator.py корректно вернул Product-0002 / Supplier-0002 как следующие свободные ID.

## Чего здесь пока нет

- GATE 4, 5, 6 (Marketing Feasibility, Demand Confirmation, Business Decision) — не реализованы, требуют более сложной логики или внешних данных (например, результата Demand Validation).
- Функция ЗАПИСИ новой записи в Knowledge Base (пока только чтение и проверка).
- Любая интеграция с внешними API (Creatify, TikTok и т.д.) — не подключены, требуют оплаты.