def shopping_list(product_list):
    if not isinstance(product_list, list):
        return None

    list_items = []
    for product in product_list:
        if isinstance(product, dict) and 'title' in product and product['title']:
            list_items.append(f"<li>{product['title']}</li>")

    return f"<ul>{''.join(list_items)}</ul>"