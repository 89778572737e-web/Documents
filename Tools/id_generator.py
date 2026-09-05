"""
Generates the next available Product-XXXX / Supplier-XXXX ID by scanning
the current Knowledge Base — prevents duplicate IDs (Decision B/D requirement).

Usage:
    export GH_TOKEN="your_github_token"
    python3 id_generator.py
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


def get_next_id(prefix: str, content: str) -> str:
    """Scans content for all IDs matching Prefix-NNNN and returns the next free one."""
    pattern = rf"{prefix}-(\d{{4}})"
    matches = re.findall(pattern, content)
    next_num = 1 if not matches else max(int(m) for m in matches) + 1
    return f"{prefix}-{next_num:04d}"


if __name__ == "__main__":
    products_content = fetch_file('Knowledge_Base/Products.md')
    suppliers_content = fetch_file('Knowledge_Base/Suppliers.md')

    print(f"Следующий свободный Product ID:  {get_next_id('Product', products_content)}")
    print(f"Следующий свободный Supplier ID: {get_next_id('Supplier', suppliers_content)}")