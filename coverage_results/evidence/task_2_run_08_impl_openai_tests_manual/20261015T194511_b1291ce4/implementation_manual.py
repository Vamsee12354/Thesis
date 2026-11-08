def get_average_price(price_list):
    try:
        valid_prices = [p['price'] for p in price_list if p.get('price') is not None]
        if not valid_prices:
            return None
        return round(sum(valid_prices) / len(valid_prices), 2)
    except Exception:
        return None