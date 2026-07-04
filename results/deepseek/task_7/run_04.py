def shopping_list(shopping_list):
    if not isinstance(shopping_list, list):
        return None
    li_elements = ''.join([f'<li>{product.get("title", "")}</li>' for product in shopping_list if isinstance(product, dict) and product.get("title")])
    return f'<ul>{li_elements}</ul>'


