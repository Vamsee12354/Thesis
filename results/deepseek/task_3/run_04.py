def get_min_2_attributes(data, dict_search):
    if not data:
        return None
    
    values = []
    for item in data:
        if dict_search in item:
            value = item[dict_search]
            if value is not None and isinstance(value, (int, float)):
                values.append(value)
    
    if not values:
        return None
    
    min_value = min(values)
    return round(float(min_value), 2)
