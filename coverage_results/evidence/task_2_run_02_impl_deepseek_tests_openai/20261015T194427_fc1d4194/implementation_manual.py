 
def get_average_price(price_list):
    if not price_list:
        return None
    
    valid_prices = []
    for product in price_list:
        if 'price' in product and product['price'] is not None:
            valid_prices.append(product['price'])
    
    if not valid_prices:
        return None
    
    average = sum(valid_prices) / len(valid_prices)
    return round(average, 2)
 