import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6JQn4O4RGa9aAHdFVHnfiQWSshpOMrTSA97lxc6eAVBoQ")
model=genai.GenerativeModel('gemini-2.5-flash')
response=model.generate_content("Write a Python function that checks if a number is prime")
print(response.text)    
