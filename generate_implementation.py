import google.generativeai as genai
genai.configure(api_key="AIzaSyCXgUmKgagtyZgs7v_2wR3f38t5gsfhlo4")
model=genai.GenerativeModel('gemini-2.5-flash')
response=model.generate_content("Write a Python function that checks if a number is prime")
print(response.text)    
