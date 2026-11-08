def get_min_2_attributes(data, dict_search):
    if not isinstance(data, list) or not isinstance(dict_search, str):
        return None
    valid_values = []
    for product in data:
        if dict_search in product and product[dict_search] is not None:
            if isinstance(product[dict_search], (int, float)):
                valid_values.append(product[dict_search])
    if not valid_values:
        return None
    return round(min(valid_values), 2)
