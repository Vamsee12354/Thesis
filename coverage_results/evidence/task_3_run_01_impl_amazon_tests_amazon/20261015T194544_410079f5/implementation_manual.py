def get_min_2_attributes(data, dict_search):
    valid_values = []
    for product in data:
        value = product.get(dict_search)
        if value is not None and isinstance(value, (int, float)):
            valid_values.append(value)
    if not valid_values:
        return None
    return round(min(valid_values), 2)
