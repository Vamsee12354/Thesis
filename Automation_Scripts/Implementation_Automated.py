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
TASK_NUMBER = input("Enter task number: ").strip()
RUNS = 10

TEMPERATURE = 0.0
TOP_P = 1.0
TOP_K = 1
SEED = 42
MAX_TOKENS = 3000
SLEEP_SECONDS = 3

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


	 


"""

TASK_DIR = os.path.join("results", LLM_NAME, f"task_{TASK_NUMBER}")
METADATA_DIR = os.path.join(TASK_DIR, "metadata")

def ensure_output_dirs():
    os.makedirs(TASK_DIR, exist_ok=True)
    os.makedirs(METADATA_DIR, exist_ok=True)


def save_run(run_number, content, usage, elapsed_time):
    run_file = os.path.join(TASK_DIR, f"run_{run_number:02d}.py")
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
        print(f"\nSaved to results/{LLM_NAME}/task_{TASK_NUMBER}/run_{i:02d}.py")
        print(f"Metadata saved to results/{LLM_NAME}/task_{TASK_NUMBER}/metadata/run_{i:02d}_meta.json")

    except Exception as error:
        print(f"ERROR IN RUN {i}: {error}")

    print(f"\n{'=' * 50}\n")
    time.sleep(SLEEP_SECONDS)