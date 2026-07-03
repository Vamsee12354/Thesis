def get_average_price(price_list):
    if not isinstance(price_list, list) or not price_list:
        return None

    valid_prices = []
    for item in price_list:
        if isinstance(item, dict) and item.get('price') is not None:
            try:
                price_value = float(item['price'])
                valid_prices.append(price_value)
            except (ValueError, TypeError):
                continue

    if not valid_prices:
        return None

    average = sum(valid_prices) / len(valid_prices)
    return round(average, 2)