def get_min_2_attributes(data, dict_search):
    if not data:
        return None
    
    valid_values = []
    for product in data:
        if dict_search in product and product[dict_search] is not None:
            value = product[dict_search]
            if isinstance(value, (int, float)):
                valid_values.append(value)
    
    if not valid_values:
        return None
    
    min_value = min(valid_values)
    return round(min_value, 2)

 #     Module Name: Get_min_attribute
# Function_Name: get_min_2_attributes
# Purpose
# •	Calculates the minimum value of a given attribute across all products .
# Useful for analysis , filtering (e .g., minimum price , minimum weight ). 
# Inputs
# •	Arguments :
# o	Dict_search
# 	It represents the attribute to extract ( e.g.:  pricemin, : battery_life, etc.).
# o	List[{data}]
# 	Data as a parameter which takes a list of dictionaries each containing various attributes.
# 	Each dictionary must have the attribute specified by dict_search for the function to work correctly.
# 	If the attribute is not present in a product, that product is ignored in the calculation.
# Output
# Return Type:
# 	o	The minimum non - None value of the given attribute across
# o	Returns None if no products contain a valid value for that attribute .
# o	Returns value in float with rounded to 2 decimals .

# Constraints
# o	Only products where get_min_2_attributes( data, dict_search) is not None are considered .
# o	The attribute must be numeric ( integer or float ).
# o	Values must be comparable using Enum . min /1.     
# Known Edge cases
# o	If all values for the given attribute are None , the function returns None.
# o	If products is an empty list , the result is also None . 

# Example Calls & Expected Outputs

#  get_min_2_attributes(data = [
#     {"price": 49.99, "battery_life": 4.0},
#     {"price": 29.99, "battery_life": 3.5},
#     {"price": None, "battery_life": 5.0},  
#     {"battery_life": 2.0}                   
# ], "price")
# # => 29.99

# get_min_2_attributes(data = [
#     {"price": 49.99, "battery_life": 4.0},
#     {"price": 29.99, "battery_life": 3.5},
#     {"price": None, "battery_life": 5.0},  
#     {"battery_life": 2.0}                   
# ], "battery_life")
# # => 2.0

# get_min_2_attributes(data = [
#     {"price": 49.99, "battery_life": 4.0},
#     {"price": 29.99, "battery_life": 3.5},
#     {"price": None, "battery_life": 5.0},  
#     {"battery_life": 2.0}                   
# ], "non_existent_field")
# # => None

# get_min_2_attributes(data = [
#     {“title”:”A”},
#     { “title”:”B”},
#     {“ title”:”C” },  
#     {"title”:”None”}, ‘title’                   
# ])
# # => None
