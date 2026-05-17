def get_min(dict):
    cheap=float("inf")
    car=""
    for x in dict:
        if dict[x] <cheap:
            cheap=dict[x]
            car=x
    return car,cheap

