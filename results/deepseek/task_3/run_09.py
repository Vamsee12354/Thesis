def get_min_2_attributes(data, dict_search):
    min_value = None
    for item in data:
        if isinstance(item, dict) and dict_search in item:
            value = item.get(dict_search)
            if value is not None and isinstance(value, (int, float)):
                if min_value is None or value < min_value:
                    min_value = value
    return round(min_value, 2) if min_value is not None else None
