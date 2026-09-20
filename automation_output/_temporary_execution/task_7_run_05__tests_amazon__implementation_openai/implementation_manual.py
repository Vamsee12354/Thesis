def shopping_list(shopping_list):
    try:
        if not isinstance(shopping_list, list):
            return None
        html_list = "<ul>"
        for product in shopping_list:
            title = product.get("title")
            if title:
                html_list += f"<li>{title}</li>"
        html_list += "</ul>"
        return html_list
    except Exception:
        return None