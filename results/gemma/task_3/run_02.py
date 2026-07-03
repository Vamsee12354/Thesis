def get_min_2_attributes(data, dict_search):
    if not isinstance(data, list) or not data:
        return None

    values = []
    for item in data:
        if not isinstance(item, dict):
            continue

        val = item.get(dict_search)

        if val is not None and isinstance(val, (int, float)):
            values.append(float(val))

    if not values:
        return None

    try:
        min_val = min(values)
        return round(float(min_val), 2)
    except (ValueError, TypeError):
        return None
