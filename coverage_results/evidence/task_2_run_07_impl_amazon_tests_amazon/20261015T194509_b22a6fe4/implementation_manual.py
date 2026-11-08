def get_average_price(price_list):
    valid_prices = [price['price'] for price in price_list if price['price'] is not None]
    if not valid_prices:
        return None
    return round(sum(valid_prices) / len(valid_prices), 2)
