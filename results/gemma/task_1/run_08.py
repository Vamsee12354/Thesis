def get_unique(brand_list):
    if not brand_list:
        return None

    seen_brands = {}
    valid_brands_found = False

    for item in brand_list:
        try:
            raw_brand = item.get('brand')
            if raw_brand is not None:
                brand_str = str(raw_brand).strip()
                if brand_str:
                    normalized = brand_str.capitalize()
                    if normalized not in seen_brands:
                        seen_brands[normalized] = normalized
                        valid_brands_found = True
        except (AttributeError, TypeError):
            continue

    if not valid_brands_found:
        return None

    result = []
    for key in seen_brands:
        result.append(seen_brands[key])

    return result