from openai import OpenAI
import json
import time

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

LLM_NAME="gemma-4-26b-a4b-it:free"
RUNS = 10

UNIVERSAL_PROMPT = """
You are an expert Python developer.

Code Style:
- Follow PEP 8 style guidelines.
- Use snake_case for variable names, function names, and file names.
- Use PascalCase for class names.
- Write concise, readable code with meaningful variable and function names.
- Do not add any text, explanation, or code fences. Return only raw Python code.
-Return plain raw Python only
- Entire response should be executable python code only. Do not include any comments or explanations
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





 




"""

for i in range(1, RUNS + 1):
    input(f"Press Enter to generate run {i}/{RUNS}...")  # ADD THIS

    print(f"\n{'=' * 20} RUN {i} {'=' * 20}\n")

    try:
        response = client.chat.completions.create(
            model=LLM_NAME,
            messages=[
                {"role": "system", "content": UNIVERSAL_PROMPT},
                {"role": "user", "content": TASK_PROMPT}
            ]
        )

        output = response.choices[0].message.content
        print(output)

    except Exception as e:
        print(f"ERROR IN RUN {i}: {e}")

    print(f"\n{'=' * 50}\n")
    time.sleep(3)  