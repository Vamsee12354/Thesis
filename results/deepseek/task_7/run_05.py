def shopping_list(shopping_list):
    if not isinstance(shopping_list, list):
        return None
    items = []
    for product in shopping_list:
        if isinstance(product, dict) and 'title' in product and product['title']:
            items.append(f"<li>{product['title']}</li>")
    return f"<ul>{''.join(items)}</ul>"