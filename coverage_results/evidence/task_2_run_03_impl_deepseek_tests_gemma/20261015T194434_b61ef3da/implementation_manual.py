def get_average_price(price_list):
    valid_prices = []
    for item in price_list:
        if isinstance(item, dict) and 'price' in item and item['price'] is not None:
            price = item['price']
            valid_prices.append(price)
    
    if not valid_prices:
        return None
    
    average = sum(valid_prices) / len(valid_prices)
    return round(average, 2)
 