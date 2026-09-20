def get_unique(brand_list):
    if not brand_list:
        return None
    
    seen_brands = {}
    unique_brands = []
    
    for item in brand_list:
        if isinstance(item, dict) and 'brand' in item:
            brand = item['brand']
            if brand and isinstance(brand, str) and brand.strip():
                normalized_brand = brand.strip().capitalize()
                if normalized_brand not in seen_brands:
                    seen_brands[normalized_brand] = True
                    unique_brands.append(normalized_brand)
    
    return unique_brands if unique_brands else None
