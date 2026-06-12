def shopping_list(products):
    items=""
    if len(products)==0:
        return "<ul></ul>"
    else:
        for i in products:
            items+=f"<li>{i}</li>"
    return f"<ul>{items}</ul>"
 
 
 
 