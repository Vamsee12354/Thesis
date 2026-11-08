def get_min_2_attributes(data, dict_search):
    if not data:
        return None
    
    values = []
    for product in data:
        if dict_search in product and product[dict_search] is not None:
            value = product[dict_search]
            if isinstance(value, (int, float)):
                values.append(value)
    
    if not values:
        return None
    
    min_value = min(values)
    return round(float(min_value), 2)
