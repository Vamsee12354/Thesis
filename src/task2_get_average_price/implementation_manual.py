price_list=[13,None,11,232,121,None,210]
filtered_price =[]
for x in price_list:
    if x is not None:
        filtered_price.append(x)

print(filtered_price)

mean_sales=sum(filtered_price)/len(filtered_price)
print(mean_sales)