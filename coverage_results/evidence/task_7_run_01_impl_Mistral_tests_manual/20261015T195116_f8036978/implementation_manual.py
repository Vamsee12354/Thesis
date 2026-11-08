def shopping_list(product_list):
    if not isinstance(product_list, list):
        return None
    html_items = []
    for product in product_list:
        if not isinstance(product, dict) or 'title' not in product:
            continue
        title = product['title']
        if title is None or not isinstance(title, str):
            continue
        html_items.append(f"<li>{title}</li>")
    return f"<ul>{''.join(html_items)}</ul>"