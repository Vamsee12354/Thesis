def shopping_list(products):
    if not products:
        return "<ul></ul>"
    list_items = "".join(f"<li>{product.get('title', '')}</li>" for product in products)
    return f"<ul>{list_items}</ul>"