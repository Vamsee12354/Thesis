def get_unique(brand_list):
    if not brand_list:
        return None

    seen_brands = {}
    valid_brand_found = False

    for item in brand_list:
        try:
            brand_val = item.get('brand')
            if brand_val is not None:
                brand_str = str(brand_val).strip()
                if brand_str!= "":
                    normalized = brand_str.capitalize()
                    if normalized not in seen_brands:
                        seen_brands[normalized] = True
                        valid_brand_found = True
        except (AttributeError, TypeError):
            continue

    if not valid_brand_found:
        return None

    result = []
    for key in seen_brands:
        result.append(key)

    return result