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

ПРИМЕЧАНИЕ: значение "Найден" входит в канонический список статусов поставщика (см. раздел Statuses выше, решено в Phase 12).

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

---

# Supplier-0002

## 1. Supplier Identity

Supplier ID:

Supplier-0002

Company Name:

Shenzhen Zhongpu Electronics Co., Ltd.

Platform:

madeinchina.com (статус Audited Supplier, 3 года на платформе; профиль SGS/BV по данным страницы)

URL:

https://www.madeinchina.com/mall/show-Slim-15W-3-in-1-Foldable-Flat-Wireless-Charger-Mobile-Phone-Holder-Magnetic-Ast-Charging-Station_435754.html

Country:

Китай (Guangdong, Шэньчжэнь)

Category:

Consumer Electronics / Phone Accessories

Primary Products:

Магнитные беспроводные зарядки, модель IP3IN1-B (3 в 1, 15 Вт)

## 2. Production

MOQ:

100 штук (подтверждено листингом)

Production Capacity:

(не указано)

Production Lead Time:

(не указано — требует прямого запроса поставщику)

Customization Available:

(не указано в листинге)

Samples Available:

(не указано — требует прямого запроса)

## 3. Pricing & Terms

Unit Price:

$12.30 за штуку (одна цена в листинге, без скидок по объёму; подтверждено листингом madeinchina.com)

Payment Terms:

(не указано — требует подтверждения у поставщика)

Volume Discounts:

(не указано в листинге)

Additional Costs:

Стоимость доставки от поставщика до склада — НЕ ПОДТВЕРЖДЕНА. Упаковка: 80 шт. в коробке, 40.4 × 38 × 21.7 см, вес брутто 12 кг.

## 4. Shipping

Shipping Method:

(не указано — требует согласования с поставщиком)

Shipping Cost:

НЕ ПОДТВЕРЖДЕНА — существенный пробел для финансового расчёта.

Shipping Time:

(не указано)

Shipping Conditions:

(не указано)

## 5. Quality Assessment

Product Quality:

Не проверено образцом.

Supply Stability:

3 года на платформе, статус Audited Supplier — косвенный сигнал, не прямая проверка.

Customer Reviews:

(не указано в извлечённых данных страницы)

Certification:

CE, RoHS, FCC по листингу; в таблице характеристик указан также Qi. Подлинность сертификатов не проверена.

## 6. Relationships

Related Products:

Product-0002

## 7. Supplier Lifecycle

Status:

Найден

## 8. Source / Evidence

Primary Source:

madeinchina.com, страница модели IP3IN1-B (реальный листинг, 2026-10-28)

Additional Sources:

(нет — сравнение с другими поставщиками не проводилось)

## 9. Data Quality

Data Classification:

Цена и MOQ — FACT/DATA (прямые данные листинга). Надёжность поставщика — ASSUMPTION.

Verification Status:

Цена/MOQ: VERIFIED по листингу. Надёжность/качество/сертификаты: NOT VERIFIED.

Missing Required Data:

Доставка, условия оплаты, сроки производства, цена образца, проверка сертификатов, сравнение с другими поставщиками.


---

# Supplier-0003

## 1. Supplier Identity

Supplier ID:

Supplier-0003

Company Name:

НЕ УКАЗАНО на странице (на листинге только «BM China»)

Platform:

alibaba.com

URL:

https://www.alibaba.com/product-introduction/BM-China-380ml-portable-mixer-blender_1600591949002.html

Country:

Китай (по платформе; город не указан)

Category:

Home & Kitchen / Small Appliances

Primary Products:

Портативный блендер 380 мл, USB-зарядка

## 2. Production

MOQ:

1500 штук (подтверждено листингом)

Production Capacity:

(не указано)

Production Lead Time:

(не указано — требует прямого запроса)

Customization Available:

Логотип, графика и упаковка (от 1500 штук) по листингу.

Samples Available:

(не указано — требует прямого запроса)

## 3. Pricing & Terms

Unit Price:

$3.50 за штуку при 1500-3299 шт.; $3.30 при 3300-6899; $3.00 от 6900 (подтверждено листингом)

Payment Terms:

(не указано — требует подтверждения)

Volume Discounts:

Да, три ступени (см. цену).

Additional Costs:

Доставка, пошлины, своя упаковка — НЕ ПОДТВЕРЖДЕНЫ.

## 4. Shipping

Shipping Method:

(не указано)

Shipping Cost:

НЕ ПОДТВЕРЖДЕНА — существенный пробел.

Shipping Time:

(не указано)

Shipping Conditions:

Литиевый аккумулятор требует особых условий перевозки — требует проверки.

## 5. Quality Assessment

Product Quality:

Не проверено образцом.

Supply Stability:

Данных нет: компания не названа, статус проверки на странице не указан.

Customer Reviews:

(не указано)

Certification:

Названа только BPA-free; никаких именных сертификатов на странице нет. Для литиевой батареи и контакта с пищей сертификаты НЕ ПОДТВЕРЖДЕНЫ.

## 6. Relationships

Related Products:

Product-0003

## 7. Supplier Lifecycle

Status:

Найден

## 8. Source / Evidence

Primary Source:

Страница модели на alibaba.com (2026-10-29)

Additional Sources:

Supplier-0004 как сравнение (другая модель)

## 9. Data Quality

Data Classification:

Цена и MOQ — FACT/DATA. Надёжность — ASSUMPTION (слабая: компания не названа).

Verification Status:

Цена/MOQ: VERIFIED по листингу. Остальное: NOT VERIFIED.

Missing Required Data:

Название компании и её проверка, сертификаты, доставка, срок производства, образец.

---

# Supplier-0004

## 1. Supplier Identity

Supplier ID:

Supplier-0004

Company Name:

Zhejiang Seabroad Household Products Co., Ltd.

Platform:

Global Sources (значки «Verified supplier» и «Standard Supplier», 2 года на платформе)

URL:

https://m.globalsources.com/Personal-mini/PERSONAL-BLENDER-1221302383p.htm

Country:

Китай (Чжэцзян, порт отгрузки Нинбо)

Category:

Home & Kitchen / Small Appliances

Primary Products:

Портативные блендеры; на странице название модели — большая ёмкость 1600 мл (НЕ тот же товар, что 380 мл)

## 2. Production

MOQ:

1000 штук (подтверждено листингом)

Production Capacity:

(не указано)

Production Lead Time:

30-45 дней по листингу

Customization Available:

Да: OEM, ODM, OBM, свой бренд, требования покупателя.

Samples Available:

Бесплатных образцов нет; стоимость возвращается после подтверждения заказа (по листингу).

## 3. Pricing & Terms

Unit Price:

$8.50 за штуку (одна цена, без ступеней; подтверждено листингом)

Payment Terms:

Банковский перевод (T/T), также аккредитив (по листингу).

Volume Discounts:

Не указаны.

Additional Costs:

Доставка до склада, пошлины — НЕ ПОДТВЕРЖДЕНЫ. Условия FOB Ningbo. Упаковка: по 12 шт. в коробке 45 x 58 x 29.5 см.

## 4. Shipping

Shipping Method:

FOB Ningbo (дальше доставку организует покупатель)

Shipping Cost:

НЕ ПОДТВЕРЖДЕНА.

Shipping Time:

(не указано)

Shipping Conditions:

Литиевый аккумулятор требует особых условий перевозки — требует проверки.

## 5. Quality Assessment

Product Quality:

Не проверено образцом.

Supply Stability:

Косвенные сигналы: статус «Verified», но на странице противоречие — год основания 2017, а в ответах написано «10 лет в бизнесе».

Customer Reviews:

(не указано)

Certification:

По листингу: EMC, TUV, LFGB, RoHS, PAHS, SCCP, PSE; заявлены BSCI/ISO9001. Подлинность не проверена.

## 6. Relationships

Related Products:

Product-0003

## 7. Supplier Lifecycle

Status:

Найден

## 8. Source / Evidence

Primary Source:

Global Sources, страница модели (2026-10-29)

Additional Sources:

Supplier-0003 как сравнение

## 9. Data Quality

Data Classification:

Цена, MOQ, срок, сертификаты — FACT/DATA по листингу. Надёжность — ASSUMPTION.

Verification Status:

Цена/MOQ/срок: VERIFIED по листингу. Сертификаты и надёжность: NOT VERIFIED.

Missing Required Data:

Доставка, проверка сертификатов, образец, цена модели 380 мл у этого поставщика.
