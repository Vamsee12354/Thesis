 

def get_min_2_attributes(data,dict_search):
    cheap=float("inf")
    for item in data:
        value=item.get(dict_search)
        if value is not None and value<cheap:
            cheap=value
    return cheap




data = [
    {"price": 49.99, "battery_life": 4.0},
    {"price": 29.99, "battery_life": 3.5},
    {"price": None, "battery_life": 5.0},  
    {"battery_life": 2.0}                   
]

min_price = get_min_2_attributes(data, "price")
print(min_price)   