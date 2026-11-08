def get_min_2_attributes(list_of_dicts, attribute):
    valid_values = []
    for product in list_of_dicts:
        try:
            value = product.get(attribute)
            if value is not None:
                valid_values.append(float(value))
        except (ValueError, TypeError):
            continue

    if not valid_values:
        return None
    return round(min(valid_values), 2)