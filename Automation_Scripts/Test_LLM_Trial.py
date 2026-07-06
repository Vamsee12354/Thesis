from openai import OpenAI
import json
import os
import time
from datetime import datetime


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)


LLM_NAME = "gemma"
MODEL_ID = "google/gemma-4-26b-a4b-it"

TASK_NUMBER = "1"
RUNS = 1

TEMPERATURE = 0.0
TOP_P = 1.0
TOP_K = 1
SEED = 42
MAX_TOKENS = 3000
SLEEP_SECONDS = 3


UNIVERSAL_PROMPT = """
Python Test Prompt
- Write clear, concise, idiomatic unittests.
- Import unittest as a library for writing tests.
- Group related test cases together to improve readability.
- Prefer assertEqual, assertTrue, assertFalse, and assertRaises for clarity.
- Ensure tests are readable and serve as documentation.
- Structure tests with clear setup, action, and verification phases (AAA pattern).
- Write tests using the exact functions or classes provided.
- Do not create or assume additional classes, objects, or wrappers that are not specified in the implementation.
- Import functions and classes only from implementation_manual.

Testing Tools
- Use unittest as the primary testing framework.
- Do not use external testing libraries unless explicitly specified.
- Ensure all tests are deterministic and do not rely on external state.
- Do not expect modules to be defined elsewhere in the implementation unless specified.

Test Coverage
- Write tests for all functions or classes mentioned.
- Include edge cases, validation failures, and happy paths.

Naming and Structure
- Use snake_case for test names and function names.
- Use descriptive test class names when using classes.
- Do not test private methods, internal state, or implementation details.
- Verify observable behaviour, outputs, and expected errors.

Output Rules
- Return only valid raw Python unittest test code.
- Do not include markdown code fences.
- Do not include explanations outside the code.
- Do not put any comments inside the code
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


TASK_DIR = os.path.join("generated_tests", LLM_NAME, f"task_{TASK_NUMBER}")
METADATA_DIR = os.path.join(TASK_DIR, "metadata")


def ensure_output_dirs():
    os.makedirs(TASK_DIR, exist_ok=True)
    os.makedirs(METADATA_DIR, exist_ok=True)


def save_run(run_number, content, usage, elapsed_time):
    run_file = os.path.join(TASK_DIR, f"run_{run_number:02d}_test.py")
    meta_file = os.path.join(METADATA_DIR, f"run_{run_number:02d}_meta.json")

    with open(run_file, "w", encoding="utf-8") as file:
        file.write(content or "")

    metadata = {
        "run_number": run_number,
        "timestamp": datetime.utcnow().isoformat(),
        "llm_name": LLM_NAME,
        "model_id": MODEL_ID,
        "task_number": TASK_NUMBER,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "top_k": TOP_K,
        "seed": SEED,
        "max_tokens": MAX_TOKENS,
        "elapsed_time_seconds": round(elapsed_time, 4),
        "usage": {
            "prompt_tokens": getattr(usage, "prompt_tokens", None),
            "completion_tokens": getattr(usage, "completion_tokens", None),
            "total_tokens": getattr(usage, "total_tokens", None)
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
                {"role": "user", "content": TASK_PROMPT}
            ]
        )

        elapsed_time = time.time() - start_time
        output = response.choices[0].message.content
        usage = getattr(response, "usage", None)

        save_run(i, output, usage, elapsed_time)

        print(output)
        print(f"\nSaved to generated_tests/{LLM_NAME}/task_{TASK_NUMBER}/run_{i:02d}_test.py")
        print(f"Metadata saved to generated_tests/{LLM_NAME}/task_{TASK_NUMBER}/metadata/run_{i:02d}_meta.json")

    except Exception as error:
        print(f"ERROR IN RUN {i}: {error}")

    print(f"\n{'=' * 50}\n")
    time.sleep(SLEEP_SECONDS)