def get_unique(brand_list):
    if not brand_list:
        return None
    
    unique_brands = {}
    
    for brand_data in brand_list:
        brand = brand_data.get('brand')
        if brand is None or brand == '':
            continue
        normalized_brand = brand.strip().capitalize()
        if normalized_brand not in unique_brands:
            unique_brands[normalized_brand] = True
    
    if not unique_brands:
        return None
    
    return list(unique_brands.keys())
