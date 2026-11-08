def shopping_list(shopping_list):
    try:
        if not isinstance(shopping_list, list):
            return None
        html_list = ''.join(f'<li>{item["title"]}</li>' for item in shopping_list if item.get("title"))
        return f'<ul>{html_list}</ul>'
    except Exception:
        return None