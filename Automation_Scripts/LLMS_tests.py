from openai import OpenAI
import json
import os
import time
from datetime import datetime


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)


LLM_NAME = "mistral"
MODEL_ID = "mistralai/mistral-small-2603"
TASK_NUMBER = "6"
RUNS = 10

TEMPERATURE = 0.0
TOP_P = 1.0
TOP_K = 1
SEED = 42
MAX_TOKENS = 6000
SLEEP_SECONDS = 3


UNIVERSAL_PROMPT = """
Output Rules
•	Write clear,concise,idiomatic unittests.
•	Import unittest as a library for writing tests
•	Group related test cases together to improve readability
•	Prefer assertEqual, assertTrue, assertFalse, and assertRaises for clarity. 
•	Ensure tests are readable and serve as documentation
•	structure tests with clear setup, action, and verification phases (AAA pattern). 
•	Write tests using the exact functions or classes provided. 
•	Do not create or assume additional classes, objects, or wrappers that are not specified in the implementation.
•	Import functions and classes only from the implementation_manual
•	Regardless of module name stated in the specification the actual file containing the implementation is always implementation_manual.py
•	Always write the import exactly as: from implementation_manual import <function_name>
•	Do not include ```python at the start or ``` at the end of the response
•	Do not include any explanations, comments about the task or any text outside the code itself.
- Do not wrap the code in Markdown fences such as ```python or ```.
- Do not begin or end the response with ```, '''python, ''', or any other delimiter.
- The first character and final character of the response must be valid Python code.


Testing Tools
•	Use unittest as primary testing framework
•	Do not use external testing libraries unless explicitly specified.
•	Ensure all tests are deterministic and do not rely on external state
•	Do not expect modules to be defined elsewhere in the implementation unless specified.
Test Coverage
•	Write tests for all functions  or classes mentioned.
•	Include edge cases, validation failures, and happy paths.
Naming and Structure
- The function name is strictly as mentioned. Do not alter it.
•	Use descriptive test class names when using classes.
•	Do not test private methods, internal state or implementation details.
•	Verify observable behaviour , outputs and expected errors.
"""


TASK_PROMPTS = {
    "1": """
Please create comprehensive Python unittest test suite within a module a Python implementation . The implementation was created based on this specification:

 SPECIFICATION :
Module Name: Unique_Brands
Function_Name: get_unique
Purpose
•	Returns a unique , filtered list of all valid brand names from the
available product dataset  in list format.
•	Eliminates duplicates and removes any None or empty string values
•	Addresses the need to extract meaningful brand information from
raw product data for display or filtering purposes . 
Inputs
•	Arguments :
o	brand_list as a parameter taking multiples names of brands
Outputs
o	Return Type:
o	List of Strings list[‘string’ ]
o	Structure :
o	 A deduplicated list of non-empty, non-None/non-Null strings from the 'brand' field.
o	Returns None if no valid brand values exist.
Constraints
o	Assumes each product dictionary contains a brand key
o	Brand values must be strings ; None and empty strings are filtered out
o	The function should ensure case - insensitivity in brand names and normalize them to a capitalized format (e.g ., " Brandname " instead of " brandname ", " BRANDNAME " , etc .)
o	No external libraries may be used for deduplication or filtering
o	Do not use sets for deduplication.
o	Use only dictionaries and/or lists.
o	Do not sort the final output list.
Known Edge cases
o	If all brand values are None or "" , the result is None
o	If get_all_products /0 returns [] , the result is also None

o	If the same brand appears in lower and upper case , it is treated as the same brand ( case - insensitive ) 

Example Calls & Expected Outputs
1. Normal case with valid brands
 get_unique({‘brand’:’Brandname1’},{‘brand’:’Brandname2’},{‘brand’:’Brandname3’})
[‘Brandname1’,’Brandname2’,’Brandname3’]
 
2. Only invalid or missing brands
	      get_unique([]) 
                   #=> None
	      3. Mixed with duplicates and blanks:
get_unique([{'brand':'Brandname'}, {'brand':'BrAnDNAme'}, {'brand':'BRANDNAME'}, {'brand':'brandname'},{'brand':None}, {'brand': ' '}])
# => ['Brandname']      

Follow the rules set with the system prompt.
The response should only contain valid Python unittest test code, without any additional text or explanations.
""",

    "2": """
Please create comprehensive Python unittest test suite within a module a Python implementation . The implementation was created based on this specification:

 SPECIFICATION :
Module Name: Get_Average_Price 
Function_Name: get_average_price():
Purpose
•	Calculates the average of the : price field from all available products
•	Excludes products with missing (None) : price values
If no valid prices are found , returns None  to indicate absence of
usable data. 
Inputs
•	Arguments :
o	price_list as a parameter taking list of dictionary of prices which has title ‘price’.
o	expected to return average price from the given list of prices with price as title. 
Outputs
o	Return Type:
o	None if no valid price exists.
o	Returns value in float with rounded to 2 decimals .
Constraints
o	Only products with non empty values : price are considered   
o	The average is calculated as sum of valid prices divided by the number of valid prices
o	No external libraries are used  
Known Edge cases
o	If get_average_price()returns [] , return None
o	If all products have price : None , returns None
o	If only one product has a price , returns that price as a float  
Example Calls & Expected Outputs
1. Normal case with valid brands
price_list=[{‘price’:100},{ ‘price’:200},{’price’:None}, {‘price’:300} ]
Valid prices : [100 , 200 , 300]
Average = 600 / 3 = 200.0
get_average_price(price_list)  #=> 200.0 
	2. With all products missing price:
price_list=[{‘price’:None},{‘price’:None}]

 
3. With no products:
	prices_list=[]
	None
Follow the rules set with the system prompt.
The response should only contain valid Python unittest test code, without any additional text or explanations.
""",

    "3": """
Please create comprehensive Python unittest test suite within a module a Python implementation . The implementation was created based on this specification:

 SPECIFICATION :
Module Name: Get_min_attribute
Function_Name: get_min_2_attributes
Purpose
•	Calculates the minimum value of a given attribute across all products .
Useful for analysis , filtering (e .g., minimum price , minimum weight ). 
Inputs
•	Arguments :
o	Dict_search
	It represents the attribute to extract ( e.g.:  pricemin, : battery_life, etc.).
o	List[{data}]
	Data as a parameter which takes a list of dictionaries each containing various attributes.
	Each dictionary must have the attribute specified by dict_search for the function to work correctly.
	If the attribute is not present in a product, that product is ignored in the calculation.
Output
Return Type:
	o	The minimum non - None value of the given attribute across
o	Returns None if no products contain a valid value for that attribute .
o	Returns value in float with rounded to 2 decimals .

Constraints
o	Only products where get_min_2_attributes( data, dict_search) is not None are considered .
o	The attribute must be numeric ( integer or float ).
o	Values must be comparable using Enum . min /1.     
Known Edge cases
o	If all values for the given attribute are None , the function returns None.
o	If products is an empty list , the result is also None . 

Example Calls & Expected Outputs

 get_min_2_attributes(data = [
    {"price": 49.99, "battery_life": 4.0},
    {"price": 29.99, "battery_life": 3.5},
    {"price": None, "battery_life": 5.0},  
    {"battery_life": 2.0}                   
], "price")
# => 29.99

get_min_2_attributes(data = [
    {"price": 49.99, "battery_life": 4.0},
    {"price": 29.99, "battery_life": 3.5},
    {"price": None, "battery_life": 5.0},  
    {"battery_life": 2.0}                   
], "battery_life")
# => 2.0

get_min_2_attributes(data = [
    {"price": 49.99, "battery_life": 4.0},
    {"price": 29.99, "battery_life": 3.5},
    {"price": None, "battery_life": 5.0},  
    {"battery_life": 2.0}                   
], "non_existent_field")
# => None

get_min_2_attributes(data = [
    {“title”:”A”},
    { “title”:”B”},
    {“ title”:”C” },  
    {"title”:”None”}, ‘title’                   
])
# => None

Follow the rules set with the system prompt.
The response should only contain valid Python unittest test code, without any additional text or explanations.
""",

    "4": """
 Please create comprehensive Python unittest test suite within a module a Python implementation . The implementation was created based on this specification:

 SPECIFICATION :
Module Name: get_read_duration
Function_Name: get_read_duration
Purpose
•	Estimates how many minutes it takes to read a blog post based on its body text .
Inputs
•	Arguments :
o	Text as a parameter which takes in a body of text.
o	The full content of the blog post as a single string .  
Outputs
o	Type: integer
o	Return Type:
o	Estimated read time in minutes , rounded up ( minimum of 1) .
Constraints
o	Assumes an average read speed of 200 words per minute 
o	Whitespace - separated tokens are considered " words ".
o	Always returns at least 1 minute , even for short or empty inputs .   
Known Edge cases
o	An empty string ("") => returns 1
o	Strings with excessive whitespace (e.g. " ") => returns 1
o	Non - latin characters (e .g. Chinese text ) may affect word counting accuracy due to the use of whitespace splitting .

Example Calls & Expected Outputs
1. Normal paragraph get_read_duration (" This is a simple blog post with about fifty words total ...") # => 1
2. Long Post
get_read_duration ( String . duplicate (" word ", 450) )
# => 3
3. Empty body
get_read_duration ("")
# => 1 
Follow the rules set with the system prompt.
The response should only contain valid Python unittest test code, without any additional text or explanations.
""",

    "5": """
Please create comprehensive Python unittest test suite within a module a Python implementation . The implementation was created based on this specification:

 SPECIFICATION :
Module Name: Form Validation
Function_Name: validate_form
Purpose
•	Validates contact form input for required fields , correct formatting , and agreement to privacy .
Inputs
o	Expected Inputs:
	First_Name
	Last_Name
	Email
	Subject
	Message
	Privacy
o	Example
	First_Name => John
	Last_Name => Marston
	Email=> john@example.com
	Subject=> Frage
	Message=> Hallo!
	Privacy=> True
Outputs
o	Success:
o	Should return:
Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}
o	Failure:
o	On failure always return a list of error messages , even if there is only one error.
o	Please Type First Name 
o	Please Type Last Name 
o	Please Type EmailID
o	Email standards not followed
o	Please Type Subject
o	Please Type Message
o	Please confirm the privacy policy

Constraints
o	“first_name”,"last_name " , " email ", " subject " , " message " must be non - empty after trimming whitespace. After trimming email and it turns out to be empty then return ”Please Type EmailID”
o	" email " must match the regex ~r /^[^\ s@ ]+ @ [^\ s@ ]+\.[^\ s@ ]+ $/ and should verify it only after trimming whitespaces.
o	error message for invalid ( non - empty ) email : Email standards not followed
o	error message for missing or invalid privacy : Please confirm the privacy policy
o	Error messages are collected as a list and multiple error messages are appended into that list.
o	" privacy " must be True. Error message for privacy not being True: Please confirm the privacy policy
o	Validations are performed in the exact order: First_Name, Last_Name, Email, Subject, Message, Privacy.
o	Error messages should be appended in the same exact order as well
Known Edge cases
o	Missing or blank fields ( including those with only whitespace) fail validation .
o	" privacy " must be a boolean : True  . Failure to that should return the error message.
o	If multiple fields are invalid , all errors are returned at once .
o	if " email " is empty it will not be validated against the regex and only show the error message for being blank  

Example Calls & Expected Outputs
1. Normal Functionality   validate_form("Alexa","James","abc@gmail.com","Question","Hallo!",True)
# => Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True
2. Rejecting Privacy Policy
validate_form("Alex",” John”,"abc@gmail.net","Question","Hallo!",False)
#=> ["Please confirm the privacy policy"]
3. Empty body
validate_form("","","","","","") 
#=> ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy']
Follow the rules set with the system prompt.
The response should only contain valid Python unittest test code, without any additional text or explanations.
""",

    "6": """
Please create comprehensive Python unittest test suite within a module a Python implementation . The implementation was created based on this specification:

 SPECIFICATION :
Module Name: Passsword Validator
Function_Name: IsValidPassword()
Purpose
•	Validates the strength and presence of a user ’s password in an Ecto changeset .
•	Ensures the password meets length and complexity requirements before account creation or update .
•	Intended to enforce secure password rules within user – facing forms or APIs
Inputs
•	Password as a parameter which takes in unique password given by the user as an input.
Outputs
o	Success:
o	 Return “The password is valid”
o	Failure:
o	Should return one or more of the following error messages in a list:
	Please fill the password
	Length must be between 12 and 72 characters
	Password must contain a lowercase letter
	Password must contain an uppercase letter
	Password must contain a special character or a number
Constraints
`IsValidPassword` is case-sensitive and must remain exactly as written.
Do NOT use `is_valid_password`.
The function name is strictly as mentioned. Do not alter it.
o	password is required and must not be None or missing .
o	password must be a string between 12 and 72 characters long
o	password must include at least :
o	one lowercase character ([a -z ])
o	one uppercase character ([A -Z ])
o	one digit or punctuation character ([!? @#$ %^&* _ 0 -9])
o	The function does not modify the password value , only validates it . 
o	Error messages are collected as a list and multiple error messages are appended into that list.
Known Edge cases
o	If : password is missing , It should append “Please fill the password” in errors list
o	If : password is shorter than 12 or longer than 72 characters , it should append message “ Length must be between 12 and 72 characters” in errors list
o	If : password lacks one of the required character types , appropriate message is appended into the errors list:
o	Password must contain a lowercase letter
o	Password must contain an uppercase letter
o	Password must contain a special character or a number

Example Calls & Expected Outputs
1. Missing Password  IsValidPassword("")
# => [“Please fill the password”]
2. Weak password
# => ['Length must be between 12 and 72 characters', 'Password must contain an uppercase letter', 'Password must contain a special character or a number']
3. Strong Password
# => “The password is valid”


Follow the rules set with the system prompt.
The response should only contain valid Python unittest test code, without any additional text or explanations.
""",

    "7": """
Please create comprehensive Python unittest test suite within a module a Python implementation . The implementation was created based on this specification:

 SPECIFICATION :
Module Name: product_list_view
Function_Name: shopping_list
Purpose
•	Takes a product list as input from the function argument and renders the title of each product inside an HTML list .
•	Addresses the need to extract meaningful brand information from
raw product data for display or filtering purposes .
Inputs
•	Parameters :
o	 shopping_list: A list of product dictionaries.
Outputs
o	HTML Structure:
o	Outputs a <ul > with <li > elements , each containing the title of a product
Constraints
o	Assumes that each product map returned includes a non - None , non - empty 
o	Titles are rendered without sanitization = > any HTML content in titles must be trusted or sanitized before assignment
o	No pagination , filtering , or interaction logic is included
Known Edge cases
o	If shopping_list returns an empty list , the <ul> will render no <li > elements rather it will return <ul></ul>.
Example Calls & Expected Outputs
1.Normal Functionality 
return shopping_list([{"title":"Item1"},{"title":"Item2"},{"title":"Item3"},{"title":"Item4"}])
# => <ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>

 
2. Empty shopping list
	      shopping_list([]) 
                   #=> <ul></ul>

Follow the rules set with the system prompt.
The response should only contain valid Python unittest test code, without any additional text or explanations.
""",

    "8": """
Task 8 
Please create comprehensive Python unittest test suite within a module a Python implementation . The implementation was created based on this specification:

 SPECIFICATION :

Module Name: Slug
Function_Name: slugify_manual()
Purpose
•	Converts any given string into a URL - friendly slug by transliterating Unicode characters into their alphanumeric equivalents . 
•	Removes or replaces punctuation and whitespace , with customizable options for separator , casing , truncation , and ignored characters .
•	Ensures SEO - friendly and standardized slugs for diverse and potentially non - ASCII inputs .
Inputs
•	Parameters :
o	text: Takes in a string which needs to be slugified
o	separator= ( binary or UTF -8 integer ): character (s) used to replace spaces between words . Default: ‘ – ‘
o	lowercase ( string ) : whether to convert the result to lowercase . Default : true
o	ignore: ( string or list of strings ): characters to preserve in the slug and skip during cleanup. Defaullt: None
o	truncate: ( positive integer ) : maximum length of the slug , truncating without breaking words .
Outputs
o	Type: String
o	Returns
o	A slugified string containing only alphanumerics and the configured separator .
o	Returns None if no valid slug can be generated (e.g .input contains only invalid characters ).
Constraints
o	Slug must include only alphanumeric characters and the configured separator . 
o	Characters listed in : ignore remain unchanged in the output .
o	Punctuation is removed unless explicitly preserved via :ignore .
o	Input must be valid UTF -8

Known Edge Cases
•	Empty input or punctuation - only input => returns None
•	Very small : truncate values (e .g., 1 or 2) may eliminate all words if none fit . 
•	Leading / trailing and repeated whitespace => cleaned up .
Example : " foo bar " => " foo - bar ".
•	Mixed - language input => transliterated where possible ( e.g.,
"\ u4f60 \ u597d " => "ni - hao " unless ignored ) .
•	Very small : truncate values (e .g., 1 or 2) may eliminate all
words if none fit

Example Calls & Expected Outputs
slugify_manual(" Hello , World !")
# => " hello - world " slugify_manual(" Madam , I ’m Adam ", separator : "")
# => " madamimadam "
slugify_manual(" StUdLy CaPs ", lowercase : false ) # => " StUdLy - CaPs "
slugify_manual (" Call me maybe ", truncate : 10)
=> " call - me "
slugify_manual("\ u4f60 \ u597d \ uff0c \ u4e16 \ u754c ", ignore : ["\ u4f60 ","\ u597d "])
# => "\ u4f60 \ u597d - shi - jie "
	
Follow the rules set with the system prompt.
The response should only contain valid Python unittest test code, without any additional text or explanations.
""",

    "9": """
Please create comprehensive Python unittest test suite within a module a Python implementation . The implementation was created based on this specification:

 SPECIFICATION :

Module Name: product_cache
Class/Function:
 Class Product_cache_get:
    def __init__(self,expiry_time):
    def set(self,key,value,ttl=None):
    def get(self,key):
    def delete(self,key):
    def cleanup(self):

Purpose
•	Stores product data in dictionary for fast retrieval .
•	Provides functions to get , set , delete , and reset cached products .
•	Solves the problem of repeated database queries for frequently accessed product data 

Inputs
•	For init
o	Expiry_time :  Time until when you want the value to remain.
•	For get
o	Key : unique identifier for the cached product
•	For set 
o	Key : unique identifier for the product
o	Value : product data to be cached 
o	ttl (optional): custom TTL in milliseconds for this specific item
•	For delete
o	key ( term ) : unique identifier of the product to remove from cache
•	For cleanup
o	No arguments
Outputs
•	Get 
o	None | value
Known Edge cases
o	If a requested key doesn ’ t exist return None.
o	Setting a value with a negative TTL immediately invalidates it
o	Calling cleanup () clears all cached items , regardless of their TTL and returns “Cleaned successfully”.
o	Calling  delete () should remove the product desired and return “deleted successfully”
Example Calls & Expected Outputs
1.Initializing cache
cache=Product_cache_get( expiry_time=60000)
# => Initialized Cache

2. Setting a value in the cache
cache.set('a','apple')

3. Getting a cached value
cache.get('a')
#=> apple

4. Getting a non - existent key
Cache.get (" non - existent ")
#=>	None

5. Setting with custom TTL (1 minute )
cache.set("fruit", {"id": "fruit", "name": "apple"}, ttl=60000)
#=>{'id': fruit', 'name': apple'}

6. Deleting a cache entry cache.delete(“a”)
#=> deleted successfully
7. clearing the entire cache
Cache.cleanup()
#=> Cleaned successfully
Follow the rules set with the system prompt.
The response should only contain valid Python unittest test code, without any additional text or explanations.
"""
}


if TASK_NUMBER not in TASK_PROMPTS:
    raise ValueError(f"Invalid TASK_NUMBER: {TASK_NUMBER}. Must be one of {list(TASK_PROMPTS.keys())}.")


TASK_DIR = os.path.join("generated_tests", LLM_NAME, f"task_{TASK_NUMBER}")
METADATA_DIR = os.path.join(TASK_DIR, "metadata")


def ensure_output_dirs():
    os.makedirs(TASK_DIR, exist_ok=True)
    os.makedirs(METADATA_DIR, exist_ok=True)


def save_run(run_number, content, usage, elapsed_time, status="success", error_message=None):
    run_file = os.path.join(TASK_DIR, f"run_{run_number:02d}_test.py")
    meta_file = os.path.join(METADATA_DIR, f"run_{run_number:02d}_meta.json")

    if content is not None:
        with open(run_file, "w", encoding="utf-8") as file:
            file.write(content)

    metadata = {
        "run_number": run_number,
        "timestamp_utc": datetime.utcnow().isoformat(),
        "llm_name": LLM_NAME,
        "model_id": MODEL_ID,
        "task_number": TASK_NUMBER,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "top_k": TOP_K,
        "seed": SEED,
        "max_tokens": MAX_TOKENS,
        "sleep_seconds": SLEEP_SECONDS,
        "session_handling": "fresh request per run",
        "status": status,
        "error_message": error_message,
        "elapsed_time_seconds": round(elapsed_time, 4),
        "output_file": f"run_{run_number:02d}_test.py" if content is not None else None,
        "usage": {
            "prompt_tokens": getattr(usage, "prompt_tokens", None) if usage else None,
            "completion_tokens": getattr(usage, "completion_tokens", None) if usage else None,
            "total_tokens": getattr(usage, "total_tokens", None) if usage else None
        }
    }

    with open(meta_file, "w", encoding="utf-8") as file:
        json.dump(metadata, file, indent=4)


ensure_output_dirs()

for i in range(1, RUNS + 1):
    print(f"\n{'=' * 20} RUN {i} {'=' * 20}\n")

    try:
        start_time = time.time()

        response = client.chat.completions.create(
            model=MODEL_ID,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            top_p=TOP_P,
            seed=SEED,
            extra_body={"top_k": TOP_K},
            messages=[
                {"role": "system", "content": UNIVERSAL_PROMPT},
                {"role": "user", "content": TASK_PROMPTS[TASK_NUMBER]}
            ]
        )

        elapsed_time = time.time() - start_time
        output = response.choices[0].message.content or ""
        usage = getattr(response, "usage", None)

        save_run(i, output, usage, elapsed_time, status="success")

        print(output)
        print(f"\nSaved to: generated_tests/{LLM_NAME}/task_{TASK_NUMBER}/run_{i:02d}_test.py")
        print(f"Metadata: generated_tests/{LLM_NAME}/task_{TASK_NUMBER}/metadata/run_{i:02d}_meta.json")

    except Exception as error:
        elapsed_time = time.time() - start_time
        save_run(i, None, None, elapsed_time, status="error", error_message=str(error))
        print(f"ERROR IN RUN {i}: {error}")

    print(f"\n{'=' * 50}\n")
    time.sleep(SLEEP_SECONDS)