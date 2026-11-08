
def get_average_price(price_list):
    new_price=[]
    cost=0
    for i in price_list:
        if i['price'] is not None:
            new_price.append(i['price'])
            cost=cost+i['price']
    if len(new_price)==0:
        return None

    average=cost/len(new_price)

    return round(average,2)
            
        
            
    
