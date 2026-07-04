 
def get_average_price(price_list):
    valid_prices = [item['price'] for item in price_list if item.get('price') is not None]
    if not valid_prices:
        return None
    average = sum(valid_prices) / len(valid_prices)
    return round(average, 2)


 