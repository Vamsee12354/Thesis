def get_min_2_attributes(dict_search, list_data):
    valid_values = []
    for product in list_data:
        if dict_search in product:
            value = product[dict_search]
            if value is not None:
                valid_values.append(value)
    if not valid_values:
        return None
    try:
        min_value = min(valid_values)
        return round(float(min_value), 2)
    except (TypeError, ValueError):
        return None