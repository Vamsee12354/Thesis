
def get_unique(brand_list):
    if not brand_list:
        return None
    
    normalized_brands = []
    seen_brands = {}
    
    for item in brand_list:
        if isinstance(item, dict) and 'brand' in item:
            brand_value = item['brand']
            if isinstance(brand_value, str) and brand_value.strip():
                normalized = brand_value.strip().capitalize()
                normalized_lower = normalized.lower()
                if normalized_lower not in seen_brands:
                    seen_brands[normalized_lower] = True
                    normalized_brands.append(normalized)
    
    return normalized_brands if normalized_brands else None
