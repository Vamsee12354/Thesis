def get_unique(brand_list):
    if not brand_list:
        return None
    
    unique_brands = {}
    result = []
    
    for item in brand_list:
        if isinstance(item, dict) and 'brand' in item:
            brand = item['brand']
            if isinstance(brand, str) and brand.strip():
                normalized_brand = brand.strip().capitalize()
                if normalized_brand not in unique_brands:
                    unique_brands[normalized_brand] = True
                    result.append(normalized_brand)
    
    return result if result else None
