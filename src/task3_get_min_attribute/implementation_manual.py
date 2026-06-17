

def get_min_2_attributes(data,dict_search):
    cheap=float("inf")
    for item in data:
        value=item.get(dict_search)
        if value is not None and value<cheap:
            cheap=value
    if cheap==float('inf'):
        return None
    return cheap
