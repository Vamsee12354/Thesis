def get_unique(brand_list):
    unique_brands = []
    normalized_brands = {}

    for item in brand_list:
        if isinstance(item, dict) and 'brand' in item:
            brand = item['brand']
        elif isinstance(item, str):
            brand = item
        else:
            brand = None

        if isinstance(brand, str) and brand.strip():
            normalized = brand.strip().capitalize()
            if normalized not in normalized_brands:
                normalized_brands[normalized] = True
                unique_brands.append(normalized)

    return unique_brands if unique_brands else None
print(get_unique (['Brandname', 'BrAnDNAme', 'BRANDNAME','brandname',None,'']))