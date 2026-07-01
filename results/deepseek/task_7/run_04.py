def shopping_list(shopping_list):
    html = "<ul>"
    for product in shopping_list:
        if isinstance(product, dict) and 'title' in product and product['title']:
            html += f"<li>{product['title']}</li>"
    html += "</ul>"
    return html