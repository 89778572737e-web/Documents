"""
Writes a new Supplier record to Suppliers.md following the KB v1.0 schema
(Suppliers_Template.md structure), automatically assigning the next free
Supplier ID. Mirror of add_product.py.

Usage:
    export GH_TOKEN="your_github_token"
    python3 add_supplier.py
"""
import os
import re
import subprocess
import json
import base64

REPO = "89778572737e-web/Documents"


def api_request(method, path, payload=None):
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError("Set GH_TOKEN environment variable before running this script.")
    cmd = ['curl', '-s', '-X', method,
           '-H', f'Authorization: Bearer {token}',
           '-H', 'Accept: application/vnd.github+json']
    if payload:
        with open('/tmp/_add_supplier_payload.json', 'w') as f:
            json.dump(payload, f)
        cmd += ['-d', '@/tmp/_add_supplier_payload.json']
    cmd.append(f'https://api.github.com/repos/{REPO}/contents/{path}')
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)


def fetch_file(path):
    data = api_request('GET', f'{path}?ref=main')
    content = base64.b64decode(data['content']).decode('utf-8')
    return content, data['sha']


def get_next_id(prefix, content):
    pattern = rf"{prefix}-(\d{{4}})"
    matches = re.findall(pattern, content)
    next_num = 1 if not matches else max(int(m) for m in matches) + 1
    return f"{prefix}-{next_num:04d}"


def format_supplier_record(supplier_id, data):
    """Formats a new supplier record matching Suppliers_Template.md schema."""
    return f"""
---

# {supplier_id}

## 1. Supplier Identity

Supplier ID:

{supplier_id}

Company Name:

{data['company_name']}

Platform:

{data.get('platform', '(не указано)')}

URL:

{data.get('url', '(не указано)')}

Country:

{data.get('country', '(не указано)')}

Category:

{data.get('category', '(не указано)')}

Primary Products:

{data.get('primary_products', '(не указано)')}

## 2. Production

MOQ:

{data.get('moq', '(не указано)')}

Production Capacity:

{data.get('production_capacity', '(не указано)')}

Production Lead Time:

{data.get('lead_time', '(не указано)')}

Customization Available:

{data.get('customization', '(не указано)')}

Samples Available:

{data.get('samples', '(не указано)')}

## 3. Pricing & Terms

Unit Price:

{data.get('unit_price', '(не указано)')}

Payment Terms:

{data.get('payment_terms', '(не указано)')}

Volume Discounts:

{data.get('volume_discounts', '(не указано)')}

Additional Costs:

{data.get('additional_costs', '(не указано)')}

## 4. Shipping

Shipping Method:

{data.get('shipping_method', '(не указано)')}

Shipping Cost:

{data.get('shipping_cost', '(не подтверждена)')}

Shipping Time:

{data.get('shipping_time', '(не указано)')}

Shipping Conditions:

{data.get('shipping_conditions', '(не указано)')}

## 5. Quality Assessment

Product Quality:

{data.get('product_quality', 'Не проверено образцом.')}

Supply Stability:

{data.get('supply_stability', '(не оценена)')}

Customer Reviews:

{data.get('customer_reviews', 'Нет данных')}

Certification:

{data.get('certification', '(не указано)')}

## 6. Relationships

Related Products:

{data.get('related_products', '(не указано)')}

## 7. Supplier Lifecycle

Status:

{data.get('status', 'Найден')}

## 8. Source / Evidence

Primary Source:

{data.get('primary_source', '(отсутствует)')}

Additional Sources:

{data.get('additional_sources', '(отсутствуют)')}

## 9. Data Quality

Data Classification:

{data.get('data_classification', 'ASSUMPTION / REQUIRES VERIFICATION')}

Verification Status:

{data.get('verification_status', 'NOT VERIFIED')}

Missing Required Data:

{data.get('missing_data', '(указать вручную после первичного заполнения)')}

## 10. Notes

Notes:

{data.get('notes', '')}"""


def add_supplier(supplier_data: dict, dry_run: bool = True):
    """
    Adds a new supplier to Suppliers.md.
    dry_run=True (default): only prints, doesn't touch GitHub.
    """
    content, sha = fetch_file('Knowledge_Base/Suppliers.md')
    next_id = get_next_id('Supplier', content)

    new_record = format_supplier_record(next_id, supplier_data)
    new_content = content.rstrip('\n') + '\n' + new_record

    print(f"Next Supplier ID: {next_id}")
    print("=" * 60)
    print("RECORD TO BE ADDED:")
    print(new_record)
    print("=" * 60)

    if dry_run:
        print("\nDRY RUN — nothing written to GitHub. Set dry_run=False to commit for real.")
        return next_id

    payload = {
        "message": f"Add {next_id} via add_supplier.py",
        "content": base64.b64encode(new_content.encode('utf-8')).decode('ascii'),
        "sha": sha,
        "branch": "main"
    }
    result = api_request('PUT', 'Knowledge_Base/Suppliers.md', payload)
    if 'commit' in result:
        print(f"\nSUCCESS — committed as {next_id}, commit sha: {result['commit']['sha']}")
    else:
        print(f"\nERROR: {result}")
    return next_id


if __name__ == "__main__":
    example_supplier = {
        "company_name": "Example Supplier Co.",
        "category": "Example Category",
    }
    add_supplier(example_supplier, dry_run=True)