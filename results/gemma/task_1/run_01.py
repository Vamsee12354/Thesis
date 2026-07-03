def get_unique(brand_list):
    if not brand_list:
        return None

    unique_brands_dict = {}
    
    for item in brand_list:
        try:
            brand_val = item.get('brand')
            if brand_val is not None:
                cleaned_brand = str(brand_val).strip()
                if cleaned_brand!= "":
                    normalized = cleaned_brand.capitalize()
                    if normalized not in unique_brands_dict:
                        unique_brands_dict[normalized] = normalized
        except (AttributeError, TypeError):
            continue

    if not unique_brands_dict:
        return None

    result = []
    for key in unique_brands_dict:
        result.append(unique_brands_dict[key])
        
    return result