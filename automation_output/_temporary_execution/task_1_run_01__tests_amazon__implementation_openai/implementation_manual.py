def get_unique(brand_list):
    try:
        if not brand_list:
            return None
        unique_brands = {}
        for product in brand_list:
            brand = product.get('brand')
            if isinstance(brand, str):
                brand_clean = brand.strip()
                if brand_clean:
                    brand_key = brand_clean.lower()
                    if brand_key not in unique_brands:
                        unique_brands[brand_key] = brand_clean.capitalize()
        if not unique_brands:
            return None
        return list(unique_brands.values())
    except Exception:
        return None