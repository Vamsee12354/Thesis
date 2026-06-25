from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

LLM_NAME = "deepseek/deepseek-chat"

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
o	Do not sort the final output list.
o	Prioritize dictionaries/lists over sets.
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
	      get_unique (['Brandname', 'BrAnDNAme', ‘BRANDNAME’, ‘brandname’,None, ‘ ‘])
      # => ['Brandname']



	

"""

response = client.chat.completions.create(
    model=LLM_NAME,
    messages=[
        {"role": "system", "content": UNIVERSAL_PROMPT},
        {"role": "user", "content": TASK_PROMPT}
    ]
)

print(response.choices[0].message.content)