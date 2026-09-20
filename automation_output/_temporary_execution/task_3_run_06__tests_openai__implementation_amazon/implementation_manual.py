def get_min_2_attributes(data, dict_search):
    if not isinstance(data, list) or not isinstance(dict_search, str):
        return None
    valid_values = []
    for product in data:
        value = product.get(dict_search)
        if value is not None and (isinstance(value, int) or isinstance(value, float)):
            valid_values.append(value)
    if not valid_values:
        return None
    return round(min(valid_values), 2)
