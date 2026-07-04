def shopping_list(shopping_list):
    html_ul_start = "<ul>"
    html_ul_end = "</ul>"
    html_li_elements = []
    
    for product in shopping_list:
        title = product.get('title')
        if title:
            html_li_elements.append(f"<li>{title}</li>")
    
    html_content = html_ul_start + ''.join(html_li_elements) + html_ul_end
    return html_content
