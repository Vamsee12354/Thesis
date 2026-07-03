def get_unique(brand_list):
    if not brand_list:
        return None

    unique_brands_map = {}
    has_valid_brand = False

    for item in brand_list:
        try:
            brand_val = item.get('brand')

            if brand_val is None:
                continue

            brand_str = str(brand_val).strip()

            if brand_str == "":
                continue

            normalized_brand = brand_str.capitalize()

            if normalized_brand not in unique_brands_map:
                unique_brands_map[normalized_brand] = normalized_brand
                has_valid_brand = True
        except (AttributeError, TypeError):
            continue

    if not has_valid_brand:
        return None

    result = []
    for key in unique_brands_map:
        result.append(unique_brands_map[key])

    return result