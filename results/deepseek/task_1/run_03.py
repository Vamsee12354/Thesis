def get_unique(*brand_list):
    if not brand_list:
        return None

    normalized_brands = []
    seen_brands = {}

    for brand_dict in brand_list:
        brand = brand_dict.get('brand')
        if isinstance(brand, str) and brand.strip():
            normalized_brand = brand.strip().capitalize()
            if normalized_brand not in seen_brands:
                seen_brands[normalized_brand] = True
                normalized_brands.append(normalized_brand)

    return normalized_brands if normalized_brands else None

print(get_unique (['Brandname', 'BrAnDNAme', 'BRANDNAME','brandname',None,'']))