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
- Use snake_case for variable names and file names. Preserve any exact function or class name specified in the task.
- Write concise, readable code with meaningful variable and function names.
- Do not add any text, explanation, or code fences. Return only raw Python code.
-Return plain raw Python only
- Never rename a function whose exact name is specified in the task.
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
- Return raw executable Python source code only.
- Do not wrap the code in Markdown fences such as ```python or ```.
- Do not begin or end the response with ```, '''python, ''', or any other delimiter.
- The first character and final character of the response must be valid Python code.

"""




TASK_PROMPT = """

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