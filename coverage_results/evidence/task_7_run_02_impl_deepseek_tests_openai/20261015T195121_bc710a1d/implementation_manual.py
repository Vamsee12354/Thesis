def shopping_list(product_list):
    if not isinstance(product_list, list):
        return '<ul></ul>'
    
    items = []
    for product in product_list:
        if isinstance(product, dict) and 'title' in product and product['title'] is not None:
            items.append(f"<li>{product['title']}</li>")
    
    return f"<ul>{''.join(items)}</ul>"
