def get_min_2_attributes(data, dict_search):
    if not data:
        return None
    
    valid_values = []
    for item in data:
        if dict_search in item and isinstance(item[dict_search], (int, float)):
            valid_values.append(item[dict_search])
    
    if not valid_values:
        return None
    
    min_value = min(valid_values)
    return round(float(min_value), 2)


