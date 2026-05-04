def get_unique(brand_list):
    unique_brand_list=[]
    for i in brand_list:
        if i not in unique_brand_list:
            unique_brand_list.append(i)
    return unique_brand_list

 
