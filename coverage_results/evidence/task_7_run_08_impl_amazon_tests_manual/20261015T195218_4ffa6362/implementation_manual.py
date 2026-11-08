def shopping_list(shopping_list):
    if not isinstance(shopping_list, list):
        return None
    
    html_output = "<ul>"
    for product in shopping_list:
        if not isinstance(product, dict) or "title" not in product or not product["title"]:
            continue
        title = product["title"]
        html_output += f"<li>{title}</li>"
    html_output += "</ul>"
    return html_output
