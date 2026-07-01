def shopping_list(product_list):
    html_list = "<ul>"
    for product in product_list:
        if isinstance(product, dict) and "title" in product:
            title = product["title"]
            if title is not None:
                html_list += f"<li>{title}</li>"
    html_list += "</ul>"
    return html_list