def get_average_price(price_list):
    valid_prices = [price for price_dict in price_list for price in (price_dict.get('price'),) if price is not None]
    if not valid_prices:
        return None
    return round(sum(valid_prices) / len(valid_prices), 2)
