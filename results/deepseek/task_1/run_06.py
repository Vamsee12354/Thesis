def get_unique(brand_list):
    if not brand_list:
        return None

    unique_brands = {}
    for item in brand_list:
        if not isinstance(item, dict):
            continue
        brand = item.get('brand')
        if isinstance(brand, str) and brand.strip():
            normalized_brand = brand.strip().capitalize()
            unique_brands[normalized_brand.lower()] = normalized_brand

    if not unique_brands:
        return None

    return list(unique_brands.values())