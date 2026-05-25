def shopping_list(products):
    items=""
    if not products:
        return False
    else:
        for i in products:
            items+=f"<li>{i}</li>"
    return f"<ul>{items}</ul>"
 
 