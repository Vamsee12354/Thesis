def get_unique(brand_list):
    if not brand_list:
        return None
    
    unique_brands = []
    seen_brands = {}
    
    for brand_data in brand_list:
        brand = brand_data.get('brand')
        if brand is None or brand == '':
            continue
        
        normalized_brand = brand.strip().capitalize()
        if normalized_brand in seen_brands:
            continue
        
        seen_brands[normalized_brand] = True
        unique_brands.append(normalized_brand)
    
    return unique_brands if unique_brands else None
