def shopping_list(shopping_list):
    if not isinstance(shopping_list, list):
        return None

    try:
        html_output = "<ul>"
        for product in shopping_list:
            if isinstance(product, dict) and "title" in product:
                title = product["title"]
                if title is not None:
                    html_output += f"<li>{title}</li>"
        html_output += "</ul>"
        return html_output
    except Exception:
        return None
