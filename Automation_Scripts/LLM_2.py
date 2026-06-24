from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

LLM_NAME ="google/gemma-3-4b-it:free"

UNIVERSAL_PROMPT = """
You are an expert Python developer.

Code Style:
- Follow PEP 8 style guidelines.
- Use snake_case for variable names, function names, and file names.
- Use PascalCase for class names.
- Write concise, readable code with meaningful variable and function names.
- Do not add any text, explanation, or markdown outside the code block. Return only raw Python code. -Do not add inline comments inside the code.
Code Structure:
- Write simple, self-contained functions.
- Do not use external libraries unless the task explicitly requires them.
- Do not generate example usage, main blocks, or print statements unless asked.

Error Handling:
- Handle edge cases where appropriate using try-except.
- Return None for invalid inputs rather than crashing silently.

Output:
- Return only the implementation code.
- Do not include explanations or comments outside the code. 

"""

TASK_PROMPT = """
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
o	If all products have price : nil , returns nil
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






"""

response = client.chat.completions.create(
    model=LLM_NAME,
    messages=[
        {"role": "system", "content": UNIVERSAL_PROMPT},
        {"role": "user", "content": TASK_PROMPT}
    ]
)

print(response.choices[0].message.content)