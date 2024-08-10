def process_data(data):
    """convert all text fields to uppercase."""
    for product in data.get('products', []):
        product['name'] = product['name'].upper()
    return data
