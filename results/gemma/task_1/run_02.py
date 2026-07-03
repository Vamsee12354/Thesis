def get_unique(brand_list):
    if not brand_list:
        return None

    unique_brands_map = {}
    valid_found = False

    for item in brand_list:
        try:
            brand_val = item.get('brand')
            if brand_val is not None:
                brand_str = str(brand_val).strip()
                if brand_str:
                    normalized = brand_str.capitalize()
                    if normalized not in unique_brands_map:
                        unique_brands_map[normalized] = normalized
                    valid_found = True
        except (AttributeError, TypeError):
            continue

    if not valid_found:
        return None

    result_list = []
    for key in unique_brands_map:
        result_list.append(unique_brands_map[key])

    return result_list
