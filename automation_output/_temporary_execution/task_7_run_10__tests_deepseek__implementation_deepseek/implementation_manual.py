def shopping_list(product_list):
    if not product_list:
        return "<ul></ul>"
    
    items_html = []
    for product in product_list:
        items_html.append(f"<li>{product['title']}</li>")
    
    return f"<ul>{''.join(items_html)}</ul>"
