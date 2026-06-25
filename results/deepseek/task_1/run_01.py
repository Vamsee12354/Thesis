def get_unique(brand_list):
    if not brand_list:
        return None
    
    unique_brands = []
    seen_brands = set()
    
    for item in brand_list:
        if isinstance(item, dict):
            brand = item.get('brand')
        else:
            brand = item
        
        if isinstance(brand, str) and brand.strip():
            normalized_brand = brand.strip().capitalize()
            if normalized_brand.lower() not in seen_brands:
                seen_brands.add(normalized_brand.lower())
                unique_brands.append(normalized_brand)
    
    return unique_brands if unique_brands else None


#  Module Name: Unique_Brands
# Function_Name: get_unique
# Purpose
# •	Returns a unique , filtered list of all valid brand names from the
# available product dataset  in list format.
# •	Eliminates duplicates and removes any None or empty string values
# •	Addresses the need to extract meaningful brand information from
# raw product data for display or filtering purposes . 
# Inputs
# •	Arguments :
# o	brand_list as a parameter taking multiples names of brands
# Outputs
# o	Return Type:
# o	List of Strings list[‘string’ ]
# o	Structure :
# o	 A deduplicated list of non-empty, non-None/non-Null strings from the 'brand' field.
# o	Returns None if no valid brand values exist.
# Constraints
# o	Assumes each product dictionary contains a brand key
# o	Brand values must be strings ; None and empty strings are filtered out
# o	The function should ensure case - insensitivity in brand names and normalize them to a capitalized format (e.g ., " Brandname " instead of " brandname ", " BRANDNAME " , etc .)
# o	No external libraries may be used for deduplication or filtering
# o	Do not sort the final output list.
# Known Edge cases
# o	If all brand values are None or "" , the result is None
# o	If get_all_products /0 returns [] , the result is also None

# o	If the same brand appears in lower and upper case , it is treated as the same brand ( case - insensitive ) 

# Example Calls & Expected Outputs
# 1. Normal case with valid brands
#  get_unique({‘brand’:’Brandname1’},{‘brand’:’Brandname2’},{‘brand’:’Brandname3’})
# [‘Brandname1’,’Brandname2’,’Brandname3’]
 
# 2. Only invalid or missing brands
# 	      get_unique([]) 
#                    #=> None
# 	      3. Mixed with duplicates and blanks:
# 	      get_unique (['Brandname', 'BrAnDNAme', ‘BRANDNAME’, ‘brandname’,None, ‘ ‘])
#       # => ['Brandname']