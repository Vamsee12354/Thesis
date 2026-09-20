def shopping_list(shopping_list):
    try:
        if not isinstance(shopping_list, list):
            return None
        html_list = ''.join(f'<li>{product["title"]}</li>' for product in shopping_list if product.get("title"))
        return f'<ul>{html_list}</ul>'
    except Exception:
        return None