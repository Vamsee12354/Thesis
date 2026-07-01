def get_unique(brand_list):
    if not brand_list:
        return None

    unique_brands = {}
    for item in brand_list:
        if isinstance(item, dict) and 'brand' in item:
            brand = item['brand']
        else:
            brand = item

        if brand is None or not isinstance(brand, str) or not brand.strip():
            continue

        normalized_brand = brand.strip().capitalize()
        unique_brands[normalized_brand.lower()] = normalized_brand

    if not unique_brands:
        return None

    return list(unique_brands.values())
print(get_unique (['Brandname', 'BrAnDNAme', 'BRANDNAME','brandname',None,'']))