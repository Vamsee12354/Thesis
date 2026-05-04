def get_min(dict):
    cheap=float("inf")
    car=""
    for x in dict:
        if dict[x] <cheap:
            cheap=dict[x]
            car=x
    return car,cheap


dict={"Mercedes":75000,"Toyota":23000,"Honda":15000,"Audi":67000,"BMV":80000}
car,cheap=get_min(dict)
print(f"The cheapest car is {car} and the price is {cheap}")