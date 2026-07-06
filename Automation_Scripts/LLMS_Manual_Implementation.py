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