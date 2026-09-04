# Suppliers Database

## Назначение

Suppliers Database — единая база поставщиков.

Здесь хранятся только данные о поставщиках. Результаты AI-оценки и анализа хранятся отдельно (см. _Analysis/).

---

# Правила базы

Каждый поставщик должен:

- иметь уникальный ID;
- пройти проверку;
- содержать оценку качества;
- иметь зафиксированные условия сотрудничества.

(Восстановлено в Phase 12 — было случайно утеряно при записи первой реальной записи поставщика; раздел "Формат записи поставщика", который также был в этом файле, НЕ восстановлен намеренно — он дублировал Suppliers_Template.md устаревшей версией схемы.)

---

# Принцип

Suppliers Database является единой системой хранения информации о поставщиках для всех AI-агентов.

---

# Supplier-0001

## 1. Supplier Identity

Supplier ID:

Supplier-0001

Company Name:

Zhejiang Naduo Commodity Co., Ltd

Platform:

Alibaba.com

URL:

https://www.alibaba.com/countrysearch/CN/packing-cubes.html (конкретный листинг: "Luggage Storage Bag Packing Cubes 8 Pcs Set Travel Organizer Bag")

Country:

Китай (Zhejiang)

Category:

Travel Accessories / Luggage Organization

Primary Products:

Packing cubes / дорожные органайзеры

## 2. Production

MOQ:

20 sets (подтверждено листингом — необычно низкий MOQ для категории, у большинства конкурентов 500-1000+ единиц)

Production Capacity:

(не указано)

Production Lead Time:

(не указано в листинге — требует прямого запроса поставщику)

Customization Available:

(не указано в общих данных листинга)

Samples Available:

(не указано — требует прямого запроса)

## 3. Pricing & Terms

Unit Price:

$3.50–3.75 за набор (подтверждено листингом Alibaba)

Payment Terms:

(не указано — стандартно для Alibaba: обычно T/T или через Alibaba Trade Assurance, требует подтверждения у конкретного поставщика)

Volume Discounts:

(не указано в найденном листинге для этого диапазона MOQ)

Additional Costs:

Стоимость доставки от поставщика до склада — НЕ ПОДТВЕРЖДЕНА (в листинге указано "Shipping fee and delivery date to be negotiated").

## 4. Shipping

Shipping Method:

(не указано — требует согласования с поставщиком)

Shipping Cost:

НЕ ПОДТВЕРЖДЕНА — существенный пробел для финансового расчёта.

Shipping Time:

(не указано)

Shipping Conditions:

Обсуждается индивидуально с поставщиком ("to be negotiated").

## 5. Quality Assessment

Product Quality:

Не проверено образцом.

Supply Stability:

5 лет присутствия на платформе Alibaba — косвенный позитивный сигнал.

Customer Reviews:

Рейтинг 4.5/5.0 на основе 238 отзывов на платформе Alibaba (не путать с отзывами конечных покупателей на Amazon — это B2B-отзывы о поставщике).

Certification:

(не указано)

## 6. Relationships

Related Products:

Product-0001

## 7. Supplier Lifecycle

Status:

Найден

ПРИМЕЧАНИЕ: используется значение "Найден" из одного из трёх ранее обнаруженных вариантов enum (см. Phase 10-12 Audit, открытый вопрос про канонический enum) — выбрано как наиболее подходящее по смыслу для текущей стадии, но формально канонический список ещё не утверждён.

## 8. Source / Evidence

Primary Source:

alibaba.com/product-detail (реальный листинг, найден через веб-поиск, сентябрь 2026)

Additional Sources:

Сопоставление с другими похожими листингами (Shangrao Xinrui Luggage Co., Zhejiang Keteng, Shenzhen Makeway и др.) для проверки, что цена/MOQ соответствуют рыночной норме, а не аномалия.

## 9. Data Quality

Data Classification:

Цена и MOQ — FACT/DATA (прямая цитата из реального листинга). Надёжность поставщика — ASSUMPTION (основана на косвенных сигналах — рейтинг, годы на платформе — не на прямой проверке образца).

Verification Status:

Цена/MOQ: VERIFIED (источник — реальный листинг). Надёжность/качество: NOT VERIFIED (требует заказа образца).

Missing Required Data:

Стоимость доставки, условия оплаты, точные сроки производства — все требуют прямого контакта с поставщиком, не были доступны из публичного листинга.

## 10. Notes

Notes:

Первая реальная запись поставщика в рамках практического теста архитектуры (сентябрь 2026). Полная методология сравнения нескольких кандидатов-поставщиков — см. _Analysis/Supplier-0001_Analysis.md.