def get_unique(brand_list):
    if not brand_list:
        return None

    unique_brands = []
    seen_brands = {}

    for item in brand_list:
        if isinstance(item, dict) and 'brand' in item:
            brand = item['brand']
        else:
            brand = item

        if brand is None or not isinstance(brand, str) or brand.strip() == '':
            continue

        normalized_brand = brand.strip().capitalize()
        if normalized_brand not in seen_brands:
            seen_brands[normalized_brand] = True
            unique_brands.append(normalized_brand)

    return unique_brands if unique_brands else None

