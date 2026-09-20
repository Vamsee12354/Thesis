def get_min_2_attributes(dict_search, list_data):
    if not list_data:
        return None

    valid_values = []
    for product in list_data:
        if dict_search in product:
            value = product[dict_search]
            if value is not None:
                try:
                    valid_values.append(float(value))
                except (TypeError, ValueError):
                    continue

    if not valid_values:
        return None

    return round(min(valid_values), 2)