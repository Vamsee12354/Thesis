def shopping_list(product_list):
    if not product_list:
        return '<ul></ul>'
    items = []
    for product in product_list:
        title = product.get('title', '')
        items.append(f'<li>{title}</li>')
    return f'<ul>{"".join(items)}</ul>'