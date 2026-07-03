def get_min_2_attributes(data, dict_search):
    if not isinstance(data, list) or not data:
        return None

    valid_values = []

    for item in data:
        try:
            if not isinstance(item, dict):
                continue

            if dict_search in item:
                val = item[dict_search]
                if val is not None and isinstance(val, (int, float)):
                    valid_values.append(float(val))
        except (TypeError, ValueError):
            continue

    if not valid_values:
        return None

    try:
        min_val = min(valid_values)
        return round(float(min_val), 2)
    except (ValueError, TypeError):
        return None