dict={"Mercedes":75000,"Toyota":23000,"Honda":15000,"Audi":67000,"BMV":80000}
cheap=0
car=""
for x in dict:
    if dict[x] <cheap:
        cheap=dict[x]
        car=x

print(f"The cheapest car is {car} and the price is {cheap}")
