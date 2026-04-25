brand_list = ["Apple","Nike","Samsung","Adidas","Apple","Coca-Cola","Amazon","Sony","Nike","Tesla","Google","Adidas","Microsoft","Disney","Samsung"]
unique_brand_list=[]
for i in brand_list:
    if i not in unique_brand_list:
        unique_brand_list.append(i)

print(unique_brand_list)