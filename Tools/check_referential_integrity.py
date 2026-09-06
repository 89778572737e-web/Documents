"""
Checks referential integrity between Products.md and Suppliers.md —
enforces Decision E/F (structured Product<->Supplier relationships).

Catches real problems like:
- A Product references a Supplier ID that doesn't exist in Suppliers.md
- A Supplier's "Related Products" references a Product ID that doesn't exist
- Duplicate IDs within the same file (shouldn't happen if id_generator.py
  and add_product.py/add_supplier.py are used correctly, but this is an
  independent safety check)

Usage:
    export GH_TOKEN="your_github_token"
    python3 check_referential_integrity.py
"""
import os
import re
import subprocess
import json
import base64

REPO = "89778572737e-web/Documents"


def fetch_file(path):
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError("Set GH_TOKEN environment variable before running this script.")
    result = subprocess.run(
        ['curl', '-s', '-H', f'Authorization: Bearer {token}',
         '-H', 'Accept: application/vnd.github+json',
         f'https://api.github.com/repos/{REPO}/contents/{path}?ref=main'],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    return base64.b64decode(data['content']).decode('utf-8')


def find_all_ids(content, prefix):
    """Finds all record IDs defined as '# Prefix-XXXX' headers (actual record definitions)."""
    return re.findall(rf"^# ({prefix}-\d{{4}})\s*$", content, re.MULTILINE)


def find_referenced_supplier_ids(products_content):
    """Finds Supplier IDs referenced FROM Product records (Supplier Relationship section)."""
    # Look for "Supplier ID:\n\nSupplier-XXXX" pattern within product records
    pattern = r"## 3\. Supplier Relationship\s*\n\s*Supplier ID:\s*\n\s*\n?(Supplier-\d{4})"
    return re.findall(pattern, products_content)


def find_referenced_product_ids(suppliers_content):
    """Finds Product IDs referenced FROM Supplier records (Related Products section)."""
    pattern = r"## 6\. Relationships\s*\n\s*Related Products:\s*\n\s*\n?(Product-\d{4})"
    return re.findall(pattern, suppliers_content)


def check_duplicates(ids, label):
    seen = set()
    duplicates = set()
    for i in ids:
        if i in seen:
            duplicates.add(i)
        seen.add(i)
    if duplicates:
        return f"FAIL: дублирующиеся {label}: {duplicates}"
    return f"OK: дублей {label} не найдено ({len(ids)} уникальных)."


if __name__ == "__main__":
    products_content = fetch_file('Knowledge_Base/Products.md')
    suppliers_content = fetch_file('Knowledge_Base/Suppliers.md')

    real_product_ids = set(find_all_ids(products_content, "Product"))
    real_supplier_ids = set(find_all_ids(suppliers_content, "Supplier"))

    print("=" * 60)
    print("REFERENTIAL INTEGRITY CHECK")
    print("=" * 60)
    print(f"\nРеальные Product ID в базе: {real_product_ids}")
    print(f"Реальные Supplier ID в базе: {real_supplier_ids}")

    # Check 1: duplicates
    print("\n--- Проверка дублей ---")
    print(check_duplicates(list(real_product_ids), "Product ID"))
    print(check_duplicates(list(real_supplier_ids), "Supplier ID"))

    # Check 2: Product -> Supplier references valid
    print("\n--- Проверка ссылок Product -> Supplier ---")
    referenced_suppliers = find_referenced_supplier_ids(products_content)
    broken = [s for s in referenced_suppliers if s not in real_supplier_ids]
    if broken:
        print(f"FAIL: товары ссылаются на несуществующих поставщиков: {broken}")
    else:
        print(f"OK: все ссылки на поставщиков ({referenced_suppliers}) действительны.")

    # Check 3: Supplier -> Product references valid
    print("\n--- Проверка ссылок Supplier -> Product ---")
    referenced_products = find_referenced_product_ids(suppliers_content)
    broken2 = [p for p in referenced_products if p not in real_product_ids]
    if broken2:
        print(f"FAIL: поставщики ссылаются на несуществующие товары: {broken2}")
    else:
        print(f"OK: все обратные ссылки ({referenced_products}) действительны.")

    print("\n" + "=" * 60)