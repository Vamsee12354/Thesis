def shopping_list(product_list):
    if not isinstance(product_list, list):
        return None
    
    li_elements = ''.join([f'<li>{product["title"]}</li>' for product in product_list if isinstance(product, dict) and 'title' in product])
    return f'<ul>{li_elements}</ul>'
