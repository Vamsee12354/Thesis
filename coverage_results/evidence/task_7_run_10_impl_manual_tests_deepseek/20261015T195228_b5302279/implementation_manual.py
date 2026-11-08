def shopping_list(products):
    items=""
    if len(products)==0:
        return "<ul></ul>"
    else:
        for i in products:
            if 'title' in i and i['title']!="":
                items+=f"<li>{i['title']}</li>"
    return f"<ul>{items}</ul>"

