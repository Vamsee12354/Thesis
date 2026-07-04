 
def get_unique(brand_list):
    if not brand_list:
        return None
    
    unique_brands = {}
    result = []
    
    for item in brand_list:
        if isinstance(item, dict):
            brand = item.get('brand')
            if isinstance(brand, str) and brand.strip():
                normalized = brand.strip().capitalize()
                if normalized.lower() not in unique_brands:
                    unique_brands[normalized.lower()] = normalized
                    result.append(normalized)
    
    return result if result else None
 