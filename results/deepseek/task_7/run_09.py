def shopping_list(product_list):
    html_ul_start = "<ul>"
    html_ul_end = "</ul>"
    html_li_elements = []

    for product in product_list:
        if isinstance(product, dict) and "title" in product and product["title"] is not None:
            title = product["title"]
            html_li_elements.append(f"<li>{title}</li>")

    html_content = html_ul_start + "".join(html_li_elements) + html_ul_end
    return html_content