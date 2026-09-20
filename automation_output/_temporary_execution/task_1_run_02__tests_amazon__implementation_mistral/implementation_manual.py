from typing import List, Dict, Optional

def get_unique(brand_list: List[Dict[str, Optional[str]]]) -> Optional[List[str]]:
    if not brand_list:
        return None

    unique_brands = {}

    for product in brand_list:
        brand = product.get('brand')
        if isinstance(brand, str) and brand.strip():
            normalized_brand = brand.strip().capitalize()
            unique_brands[normalized_brand] = None

    if not unique_brands:
        return None

    return list(unique_brands.keys())