def get_min_2_attributes(data, dict_search):
    if not isinstance(data, list) or not data:
        return None

    valid_values = []

    for item in data:
        if not isinstance(item, dict):
            continue

        value = item.get(dict_search)

        if value is not None and isinstance(value, (int, float)):
            valid_values.append(float(value))

    if not valid_values:
        return None

    try:
        min_val = min(valid_values)
        return round(float(min_val), 2)
    except (ValueError, TypeError):
        return None