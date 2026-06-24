import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []
    
    if not first_name or not first_name.strip():
        errors.append("Please Type First Name")
    
    if not last_name or not last_name.strip():
        errors.append("Please Type Last Name")
    
    if not email or not email.strip():
        errors.append("Please Type EmailID")
    else:
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_regex, email.strip()):
            errors.append("Email standards not followed")
    
    if not subject or not subject.strip():
        errors.append("Please Type Subject")
    
    if not message or not message.strip():
        errors.append("Please Type Message")
    
    if not isinstance(privacy, bool) or not privacy:
        errors.append("Please confirm the privacy policy")

    if not errors:
        return f"Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}"
    else:
        return errors


# TASK_PROMPT = """

# Module Name: Form Validation
# Function_Name: Validate_form
# Purpose
# •	Validates contact form input for required fields , correct formatting , and agreement to privacy .
# Inputs
# o	Expected Keys:
# 	First_Name
# 	Last_Name
# 	Email
# 	Subject
# 	Message
# 	Privacy
# o	Example
# 	First_Name => John
# 	Last_Name => Marston
# 	Email=> john@example.com
# 	Subject=> Frage
# 	Message=> Hallo!
# 	Privacy=> True
# Outputs
# o	Success:
# o	Should return:
# Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}
# o	Failure:
# o	On failure always return a list of error messages , even if there is only one error.
# o	Please Type First Name 
# o	Please Type Last Name 
# o	Please Type EmailID
# o	Email standards not followed
# o	Please Type Subject
# o	Please Type Message
# o	Please confirm the privacy policy

# Constraints
# o	“first_name”,"last_name " , " email ", " subject " , " message " must be non - empty after trimming whitespace. After trimming email and it turns out to be empty then return ”Please Type EmailID”
# o	" email " must match the regex ~r /^[^\ s@ ]+ @ [^\ s@ ]+\.[^\ s@ ]+ $/.
# o	error message for invalid ( non - empty ) email : Email standards not followed
# o	error message for missing or invalid privacy : Please confirm the privacy policy
# o	Error messages are collected as a list and multiple error messages are appended into that list.
# o	" privacy " must be True. Error message for privacy not being True: Please confirm the privacy policy
# o	Validations are performed in the exact order: First_Name, Last_Name, Email, Subject, Message, Privacy.
# o	Error messages should be appended in the same exact order as well
# Known Edge cases
# o	Missing or blank fields ( including those with only whitespace) fail validation .
# o	" privacy " must be a boolean : True  . Failure to that should return the error message.
# o	If multiple fields are invalid , all errors are returned at once .
# o	if " email " is empty it will not be validated against the regex and only show the error message for being blank  

# Example Calls & Expected Outputs
# 1. Normal Functionality   validate_form("Alexa","James","abc@gmail.com","Question","Hallo!",True)
# # => Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True
# 2. Rejecting Privacy Policy
# validate_form("Alex",” John”,"abc@gmail.net","Question","Hallo!",False)
# #=> ["Please confirm the privacy policy"]
# 3. Empty body
# validate_form("","","","","","") 
# #=> ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy']
