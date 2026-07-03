def get_unique(brand_list):
    if not brand_list:
        return None

    unique_brands_map = {}
    has_valid_brand = False

    for item in brand_list:
        try:
            if not isinstance(item, dict):
                continue

            brand_val = item.get('brand')

            if brand_val is None:
                continue

            if not isinstance(brand_val, str):
                continue

            cleaned_brand = brand_val.strip()

            if cleaned_brand == "":
                continue

            normalized_brand = cleaned_brand.capitalize()

            if normalized_brand not in unique_brands_map:
                unique_brands_map[normalized_brand] = normalized_brand
                has_valid_brand = True
        except Exception:
            continue

    if not has_valid_brand:
        return None

    result = []
    for key in unique_brands_map:
        result.append(unique_brands_map[key])

    return result