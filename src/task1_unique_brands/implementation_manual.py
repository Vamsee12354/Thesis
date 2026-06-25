def get_unique(brand_list):
    list12={}
    for i in brand_list:
        brand=i.get('brand')
        if brand is not None and brand !="" and brand.lower() not in list12: 
            list12[brand.lower()]=brand.capitalize()
    if len(list12)==0:
        return None
    return list(list12.values())

 