def shopping_list(shopping_list):
    if not isinstance(shopping_list, list):
        return None

    html_parts = ["<ul>"]

    for product in shopping_list:
        try:
            if isinstance(product, dict) and "title" in product and product["title"]:
                title = str(product["title"])
                html_parts.append(f"<li>{title}</li>")
        except (TypeError, AttributeError):
            continue

    html_parts.append("</ul>")
    return "".join(html_parts)