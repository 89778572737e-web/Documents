# KB Tools — Real Automation (Phase 13)

Реальный, протестированный код (сентябрь 2026). Всё работает на настоящих данных из Knowledge Base, не на выдумках.

## Файлы

- `quality_gates.py` — GATE 1 (Product Data Completeness), GATE 2 (Supplier Verification), GATE 3 (Financial Viability, non-blocking, всегда считает % маржи).
- `gate_4_and_6.py` — GATE 4 (Marketing Feasibility) и GATE 6 (Business Decision — аггрегатор рекомендаций, НЕ автоматическое решение).
- `demand_scoring.py` — Demand Scoring Engine, формула Early Signal Score из Demand_Validation_Agent/README.md. Протестирован на синтетических данных (реальных экспериментов ещё нет — нет подключённых аккаунтов/API).
- `id_generator.py` — генерирует следующий свободный Product-XXXX / Supplier-XXXX ID, сканируя реальную базу.
- `add_product.py` — ЗАПИСЫВАЕТ новый товар в Products.md с автоматическим ID. По умолчанию dry_run=True (ничего не пишет, только показывает, что было бы записано) — нужно явно передать dry_run=False для реальной записи.
- `run_full_audit.py` — прогоняет ВСЕ реализованные gates по всем товарам в базе разом, выдаёт сводный отчёт.

## Как использовать

```bash
export GH_TOKEN="ваш_персональный_токен_github"
python3 run_full_audit.py
```

Токен НЕ хранится в коде — передаётся через переменную окружения (это стандартная практика безопасности, чтобы токен не утёк, если репозиторий публичный).

## Проверено на реальных данных (не выдумано)

- `quality_gates.py`: маржинальность Product-0001 = 56.1%, совпадает с ручным расчётом в _Analysis/Product-0001_Analysis.md.
- `id_generator.py`: корректно вернул Product-0002/Supplier-0002 как следующие свободные ID при реальном Product-0001/Supplier-0001 в базе.
- `add_product.py`: протестирован в dry_run режиме — корректно сформировал полную запись Product-0002 по схеме, ничего не записав без явного разрешения.
- `run_full_audit.py`: запущен end-to-end на реальной базе — честно показал, что GATE 4 (маркетинг) для Product-0001 не пройден, потому что маркетинговый анализ ещё не проводился.

## Чего здесь ещё нет

- GATE 5 (Demand Confirmation) — логика (demand_scoring.py) написана и протестирована на синтетических данных, но не подключена к реальным DemandExperiment записям, потому что таких записей ещё не существует (нет подключённых API/аккаунтов, см. Demand_Validation_Agent/README.md).
- Никакой интеграции с внешними платными API (Creatify, TikTok Content Posting API и т.д.) — требуют оплаты и разработческой регистрации, не сделаны.
- add_supplier.py (аналог add_product.py для поставщиков) — ещё не написан.
- Автоматический непрерывный мониторинг трендов (роль Product Hunter) — не реализован, требует постоянно работающей инфраструктуры.