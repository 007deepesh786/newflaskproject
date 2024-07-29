import json
def load_json():
    with open('products.json') as f:
        return json.load(f)
db = load_json()