def get_min_2_attributes(data, dict_search):
    if not data:
        return None
    
    valid_values = []
    for item in data:
        if isinstance(item, dict) and dict_search in item:
            value = item.get(dict_search)
            if value is not None and isinstance(value, (int, float)):
                valid_values.append(value)
    
    if not valid_values:
        return None
    
    return round(min(valid_values), 2)
