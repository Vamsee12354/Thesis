def get_unique(brand_list):
    unique_brand_list=[]
    for i in brand_list:
        if i not in unique_brand_list:
            unique_brand_list.append(i)
    if len(unique_brand_list) == 0:
        return []
    elif len(unique_brand_list) == len(brand_list):
        return (unique_brand_list)
    else:
        return (unique_brand_list)
    

 