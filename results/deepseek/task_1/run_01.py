def get_unique(brand_list):
    if not brand_list:
        return []

    unique_brands = set()
    for brand in brand_list:
        if isinstance(brand, str) and brand.strip():
            normalized_brand = brand.strip().capitalize()
            unique_brands.add(normalized_brand)

    return sorted(unique_brands)



# task prompt= Module Name: Unique_Brands
# Function_Name: get_unique
# Purpose
# •	Returns a unique , filtered list of all valid brand names from the
# available product dataset .
# •	Eliminates duplicates and removes any Null/None or empty string values
# •	Addresses the need to extract meaningful brand information from
# raw product data for display or filtering purposes . 
# Inputs
# •	Arguments :
# o	brand_list as a parameter taking multiples names of brands
# •	Dependency:
# o	Calls get_unique function , expected to return a list of unique brands
# Outputs
# o	Return Type:
# o	List of Strings list[‘string’ ]
# o	Structure :
# o	 A deduplicated list of non-empty, non-None/non-Null strings from the 'brand' field.
# o	Returns an empty list `[]` if no valid brand values exist.
# Constraints
# o	Assumes each product list contains a brand key
# o	Brand values must be strings ; Null/None and empty strings are filtered out
# o	The function should ensure case - insensitivity in brand names and normalize them to a capitalized format (e.g ., " Brandname " instead of " brandname ", " BRANDNAME " , etc .)
# o	No external libraries may be used for deduplication or filtering
# Known Edge cases
# o	If all brand values are nil or "" , the result is []
# o	If get_all_products /0 returns [] , the result is also []
# o	If the same brand appears in lower and upper case , it is treated as the same brand ( case - insensitive ) 

# Example Calls & Expected Outputs
# 1. Normal case with valid brands
#  get_unique ([" Brandname1 ", " Brandname2 ", " Brandname3 "])
 
# 2. Only invalid or missing brands
# 	      get_unique([]) 
#                    #=> []
# 	      3. Mixed with duplicates and blanks:
# 	      get_unique (['Brandname', 'BrAnDNAme', ‘BRANDNAME’, ‘brandname’,None, ‘ ‘])
#       # => ['Brandname']
