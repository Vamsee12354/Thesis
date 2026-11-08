def get_unique(brand_list):
    seen = {}
    for product in brand_list:
        brand = product.get('brand')
        if brand is None:
            continue
        if not isinstance(brand, str):
            continue
        brand = brand.strip()
        if not brand:
            continue
        normalized = brand.capitalize()
        if normalized not in seen:
            seen[normalized] = normalized
    if not seen:
        return None
    return list(seen.values())
