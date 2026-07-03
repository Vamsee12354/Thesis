def shopping_list(shopping_list):
    if not isinstance(shopping_list, list):
        return None

    try:
        html_parts = ["<ul>"]
        for product in shopping_list:
            if isinstance(product, dict) and "title" in product:
                title = product["title"]
                if title is not None:
                    html_parts.append(f"<li>{title}</li>")
        html_parts.append("</ul>")
        return "".join(html_parts)
    except Exception:
        return None