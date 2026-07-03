def shopping_list(shopping_list):
    if not isinstance(shopping_list, list):
        return None

    html_output = "<ul>"
    try:
        for product in shopping_list:
            if isinstance(product, dict) and product.get("title"):
                html_output += f"<li>{product['title']}</li>"
        html_output += "</ul>"
        return html_output
    except Exception:
        return None