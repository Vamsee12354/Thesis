def shopping_list(shopping_list):
    if not isinstance(shopping_list, list):
        return None
    
    if not all(isinstance(item, dict) and "title" in item for item in shopping_list):
        return None
    
    html_list = "<ul>"
    for product in shopping_list:
        if "title" in product and product["title"]:
            html_list += f"<li>{product['title']}</li>"
    html_list += "</ul>"
    return html_list
