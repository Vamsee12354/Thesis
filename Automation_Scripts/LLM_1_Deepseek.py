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

response = client.chat.completions.create(
    model=LLM_NAME,
    messages=[
        {"role": "system", "content": UNIVERSAL_PROMPT},
        {"role": "user", "content": TASK_PROMPT}
    ]
)

print(response.choices[0].message.content)