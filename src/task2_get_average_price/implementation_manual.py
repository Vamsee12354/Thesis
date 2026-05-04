def get_average(price_list):
    filtered_price =[]
    for x in price_list:
        if x is not None:
            filtered_price.append(x)

    mean_sales=sum(filtered_price)/len(filtered_price)
    return mean_sales

 