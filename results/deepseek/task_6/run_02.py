def is_valid_password(password):
    errors = []
    
    if not password:
        return "Please fill the password"
    
    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")
    
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit_or_special = any(c.isdigit() or not c.isalnum() for c in password)
    
    if not has_lower:
        errors.append("Password must contain a lowercase letter")
    if not has_upper:
        errors.append("Password must contain an uppercase letter")
    if not has_digit_or_special:
        errors.append("Password must contain a special character or a number")
    
    if not errors:
        return "The password is valid"
    else:
        return errors

# Module Name: Passsword Validator
# Function_Name: IsValidPassword()
# Purpose
# •	Validates the strength and presence of a user ’s password in an Ecto changeset .
# •	Ensures the password meets length and complexity requirements before account creation or update .
# •	Intended to enforce secure password rules within user – facing forms or APIs
# Inputs
# •	Password as a parameter which takes in unique password given by the user as an input.
# Outputs
# o	Success:
# o	Return “The password is valid”
# o	Failure:
# o	Should return one or more of the following error messages in a list:
# 	Please fill the password
# 	Length must be between 12 and 72 characters
# 	Password must contain a lowercase letter
# 	Password must contain an uppercase letter
# 	Password must contain a special character or a number
# Constraints
# o	password is required and must not be None or missing .
# o	password must be a string between 12 and 72 characters long
# o	password must include at least :
# o	one lowercase character ([a -z ])
# o	one uppercase character ([A -Z ])
# o	one digit or punctuation character ([!? @#$ %^&* _ 0 -9])
# o	The function does not modify the password value , only validates it . 
# o	Error messages are collected as a list and multiple error messages are appended into that list.
# Known Edge cases
# o	If : password is missing , It should return “Please fill the password”
# o	If : password is shorter than 12 or longer than 72 characters , it should return  message “ Length must be between 12 and 72 characters”
# o	If : password lacks one of the required character types , appropriate message is added
# o	Password must contain a lowercase letter
# o	Password must contain an uppercase letter
# o	Password must contain a special character or a number

# Example Calls & Expected Outputs
# 1. Missing Password  IsValidPassword("")
# # => Please fill the password
# 2. Weak password
# # => ['Length must be between 12 and 72 characters', 'Password must contain an uppercase letter', 'Password must contain a special character or a number']
# 3. Strong Password
# # => The password is valid
 

