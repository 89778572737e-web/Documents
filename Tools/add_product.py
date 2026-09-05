"""
Writes a new Product record to Products.md following the KB v1.0 schema
(Products_Template.md structure), automatically assigning the next free
Product ID (via id_generator.py logic) — prevents duplicate IDs.

Usage:
    export GH_TOKEN="your_github_token"
    python3 add_product.py
    (edit the `new_product` dict below before running for real use)
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
        with open('/tmp/_add_product_payload.json', 'w') as f:
            json.dump(payload, f)
        cmd += ['-d', '@/tmp/_add_product_payload.json']
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


def format_product_record(product_id, data):
    """Formats a new product record matching Products_Template.md schema."""
    return f"""
---

# {product_id}

## 1. Product Identity

Product ID:

{product_id}

Name:

{data['name']}

Category:

{data['category']}

Subcategory:

{data.get('subcategory', '(не указано)')}

## 2. Product Core Data

Description:

{data['description']}

Primary Customer Problem:

{data.get('customer_problem', '(не подтверждено независимо)')}

Product Solution:

{data.get('solution', '(не подтверждено независимо)')}

Key Features:

{data.get('features', '(не подтверждено независимо)')}

Advantages:

{data.get('advantages', '(не подтверждено независимо)')}

Disadvantages:

{data.get('disadvantages', '(не подтверждено независимо)')}

Unique Features:

{data.get('unique_features', '(не указано)')}

Improvement Opportunities:

{data.get('improvement_opportunities', '(не подтверждено независимо)')}

## 3. Supplier Relationship

Supplier ID:

{data.get('supplier_id', '(не указано)')}

## 4. Product Lifecycle

Status:

{data.get('status', 'Исследуется')}

## 5. Source / Evidence

Primary Source:

{data.get('primary_source', '(отсутствует)')}

Additional Sources:

{data.get('additional_sources', '(отсутствуют)')}

## 6. Data Quality

Data Classification:

{data.get('data_classification', 'ASSUMPTION / REQUIRES VERIFICATION')}

Verification Status:

{data.get('verification_status', 'NOT VERIFIED')}

Missing Required Data:

{data.get('missing_data', '(указать вручную после первичного заполнения)')}

## 7. Notes

Notes:

{data.get('notes', '')}"""


def add_product(product_data: dict, dry_run: bool = True):
    """
    Adds a new product to Products.md.
    dry_run=True (default): only prints what WOULD be written, doesn't touch GitHub.
    Set dry_run=False to actually commit.
    """
    content, sha = fetch_file('Knowledge_Base/Products.md')
    next_id = get_next_id('Product', content)

    new_record = format_product_record(next_id, product_data)
    new_content = content.rstrip('\n') + '\n' + new_record

    print(f"Next Product ID: {next_id}")
    print("=" * 60)
    print("RECORD TO BE ADDED:")
    print(new_record)
    print("=" * 60)

    if dry_run:
        print("\nDRY RUN — nothing written to GitHub. Set dry_run=False to commit for real.")
        return next_id

    payload = {
        "message": f"Add {next_id} via add_product.py",
        "content": base64.b64encode(new_content.encode('utf-8')).decode('ascii'),
        "sha": sha,
        "branch": "main"
    }
    result = api_request('PUT', 'Knowledge_Base/Products.md', payload)
    if 'commit' in result:
        print(f"\nSUCCESS — committed as {next_id}, commit sha: {result['commit']['sha']}")
    else:
        print(f"\nERROR: {result}")
    return next_id


if __name__ == "__main__":
    # Example — edit before real use
    example_product = {
        "name": "Example Product Name",
        "category": "Example Category",
        "description": "Example description.",
    }
    add_product(example_product, dry_run=True)