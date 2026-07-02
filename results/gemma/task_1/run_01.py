def get_unique(brand_list):
    if not brand_list:
        return None

    unique_brands = []
    seen_normalized = []

    for item in brand_list:
        try:
            if isinstance(item, dict):
                brand_val = item.get('brand')
            else:
                brand_val = item

            if brand_val is None:
                continue

            brand_str = str(brand_val).strip()

            if not brand_str:
                continue

            normalized = brand_str.capitalize()

            if normalized not in seen_normalized:
                seen_normalized.append(normalized)
                unique_brands.append(normalized)
        except (AttributeError, TypeError):
            continue

    if not unique_brands:
        return None

    return unique_brands