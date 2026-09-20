def get_average_price(price_list):
    valid_prices = [price for price in price_list if price.get('price') is not None]
    if not valid_prices:
        return None
    total_price = sum(price['price'] for price in valid_prices)
    count = len(valid_prices)
    if count == 0:
        return None
    average_price = total_price / count
    return round(average_price, 2)
