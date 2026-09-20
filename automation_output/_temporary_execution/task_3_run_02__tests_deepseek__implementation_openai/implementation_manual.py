def get_min_2_attributes(data, dict_search):
    try:
        values = [
            float(item[dict_search])
            for item in data
            if dict_search in item and item[dict_search] is not None and isinstance(item[dict_search], (int, float))
        ]
        if not values:
            return None
        return round(min(values), 2)
    except (TypeError, ValueError):
        return None