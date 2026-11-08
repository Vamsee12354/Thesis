
def get_unique(brand_list):
    if not brand_list:
        return None
    
    unique_brands = {}
    result = []
    
    for product in brand_list:
        if not isinstance(product, dict):
            continue
        brand = product.get('brand')
        if brand is None:
            continue
        if not isinstance(brand, str):
            continue
        brand = brand.strip()
        if not brand:
            continue
        normalized_brand = brand.capitalize()
        if normalized_brand not in unique_brands:
            unique_brands[normalized_brand] = True
            result.append(normalized_brand)
    
    return result if result else None
