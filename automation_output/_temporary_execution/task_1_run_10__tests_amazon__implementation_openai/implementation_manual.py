def get_unique(brand_list):
    try:
        if not brand_list:
            return None
        unique_brands = {}
        for product in brand_list:
            brand = product.get('brand')
            if isinstance(brand, str):
                normalized = brand.strip()
                if normalized:
                    key = normalized.lower()
                    if key not in unique_brands:
                        unique_brands[key] = normalized.capitalize()
        if not unique_brands:
            return None
        return list(unique_brands.values())
    except Exception:
        return None