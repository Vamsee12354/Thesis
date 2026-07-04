def get_min_2_attributes(data, dict_search):
    if not data:
        return None
    
    valid_values = []
    for item in data:
        if dict_search in item and item[dict_search] is not None:
            value = item[dict_search]
            if isinstance(value, (int, float)):
                valid_values.append(value)
    
    if not valid_values:
        return None
    
    min_value = min(valid_values)
    return round(min_value, 2)
