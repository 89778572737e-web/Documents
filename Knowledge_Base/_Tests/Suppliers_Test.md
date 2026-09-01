# Suppliers Test Database

Тестовые записи поставщиков, изолированные от production Suppliers.md согласно Decision G (Test / Production Separation).

Эти записи не должны попадать в production-выборку поставщиков.

Core Data приведена к схеме KB v1.0 (Phase 5). Результаты анализа перенесены в _Analysis/TEST-SUPPLIER-001_Analysis.md согласно принципу Decision M (применён по аналогии к Supplier).

---

# TEST-SUPPLIER-001

## 1. Supplier Identity

Supplier ID:

TEST-SUPPLIER-001

Company Name:

Test Outdoor Manufacturing

Platform:

Тестовая запись

URL:

Не указана

Country:

(не указано)

Category:

Outdoor / Travel Accessories

Primary Products:

Аксессуары для путешествий и хранения

## 2. Production

MOQ:

500 единиц

Production Capacity:

(не указано)

Production Lead Time:

Требует проверки

Customization Available:

(не указано)

Samples Available:

(не указано)

## 3. Pricing & Terms

Unit Price:

Требует уточнения

Payment Terms:

Требует проверки

Volume Discounts:

(не указано)

Additional Costs:

(не указано)

## 4. Shipping

Shipping Method:

(не указано)

Shipping Cost:

(не указано)

Shipping Time:

(не указано)

Shipping Conditions:

Требует проверки

## 5. Quality Assessment

Product Quality:

Требует проверки образца

Supply Stability:

Не оценена

Customer Reviews:

Нет данных

Certification:

(не указано)

## 6. Relationships

Related Products:

TEST-001

## 7. Supplier Lifecycle

Status:

Тестовый анализ завершён — ПРИМЕЧАНИЕ: это значение не соответствует ни одному из известных вариантов Supplier Status enum, обнаруженных в репозитории (см. Stage 5 findings). Требует отдельного решения по каноническому enum, прежде чем считать статус валидным.

## 8. Source / Evidence

Primary Source:

(отсутствует)

Additional Sources:

(отсутствуют)

## 9. Data Quality

Data Classification:

ASSUMPTION / REQUIRES VERIFICATION

Verification Status:

NOT VERIFIED

Missing Required Data:

Country, Production Capacity, Customization Available, Samples Available, Volume Discounts, Additional Costs, Shipping Method, Shipping Cost, Certification, Primary Source

## 10. Notes

Notes:

Полная история анализа (Анализ поставщика, Оценка AI) перенесена в _Analysis/TEST-SUPPLIER-001_Analysis.md при миграции KB v1.0 (Phase 5).