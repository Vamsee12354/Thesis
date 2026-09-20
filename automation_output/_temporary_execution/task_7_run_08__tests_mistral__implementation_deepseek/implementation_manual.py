def shopping_list(product_list):
    html_parts = ['<ul>']
    
    if product_list:
        for product in product_list:
            title = product.get('title', '')
            html_parts.append(f'<li>{title}</li>')
    
    html_parts.append('</ul>')
    return ''.join(html_parts)
