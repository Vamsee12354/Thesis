def shopping_list(shopping_list):
    if not isinstance(shopping_list, list):
        return None

    html_list = ['<ul>']
    for product in shopping_list:
        if isinstance(product, dict) and 'title' in product and product['title'] is not None:
            html_list.append(f'<li>{product["title"]}</li>')
    html_list.append('</ul>')
    return ''.join(html_list)