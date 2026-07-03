def get_average_price(price_list):
    if not isinstance(price_list, list) or not price_list:
        return None

    valid_prices = []
    for item in price_list:
        try:
            price = item.get('price')
            if price is not None:
                valid_prices.append(float(price))
        except (TypeError, ValueError):
            continue

    if not valid_prices:
        return None

    average = sum(valid_prices) / len(valid_prices)
    return round(float(average), 2)