def get_unique(brand_list):
    if not brand_list:
        return None

    unique_brands = {}
    for product in brand_list:
        if not isinstance(product, dict):
            continue
        brand = product.get('brand')
        if isinstance(brand, str) and brand.strip():
            normalized_brand = brand.strip().capitalize()
            unique_brands[normalized_brand.lower()] = normalized_brand

    if not unique_brands:
        return None

    return list(unique_brands.values())