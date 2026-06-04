def get_average(price_list):
    filtered_price =[]
    for x in price_list:
        if x is not None and x >= 0:
            filtered_price.append(x)
        
    mean_sales=sum(filtered_price)/len(filtered_price)
    return round(mean_sales, 2)

print(get_average([-5,-2]))