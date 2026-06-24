def get_average_price(price_list):
    valid_prices = []
    for item in price_list:
        if isinstance(item, dict) and 'price' in item and isinstance(item['price'], (int, float)):
            valid_prices.append(item['price'])
    if not valid_prices:
        return None
    average = sum(valid_prices) / len(valid_prices)
    return round(average, 2)
 # prompt=Module Name: Get_Average_Price 
# Function_Name: get_average_price():
# Purpose
# •	Calculates the average of the : price field from all available products
# •	Excludes products with missing (None) : price values
# If no valid prices are found , returns None  to indicate absence of
# usable data. 
# Inputs
# •	Arguments :
# o	price_list as a parameter taking list of dictionary of prices which has title ‘price’.
# o	expected to return average price from the given list of prices with price as title. 
# Outputs
# o	Return Type:
# o	None if no valid price exists.
# o	Returns value in float with rounded to 2 decimals .
# Constraints
# o	Only products with non empty values : price are considered   
# o	The average is calculated as sum of valid prices divided by the number of valid prices
# o	No external libraries are used  
# Known Edge cases
# o	If get_average_price()returns [] , return None
# o	If all products have price : nil , returns nil
# o	If only one product has a price , returns that price as a float  
# Example Calls & Expected Outputs
# 1. Normal case with valid brands
# price_list=[{‘price’:100},{ ‘price’:200},{’price’:None}, {‘price’:300} ]
# Valid prices : [100 , 200 , 300]
# Average = 600 / 3 = 200.0
# get_average_price(price_list)  #=> 200.0 
# 	2. With all products missing price:
# price_list=[{‘price’:None},{‘price’:None}]

 
# 3. With no products:
# 	prices_list=[]
# 	None

