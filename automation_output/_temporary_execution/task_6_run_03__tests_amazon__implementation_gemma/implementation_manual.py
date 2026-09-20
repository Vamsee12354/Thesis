import re

def IsValidPassword(password):
    if password is None or password == "":
        return ["Please fill the password"]

    errors = []

    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")

    if not re.search(r"[a-z]", password):
        errors.append("Password must contain a lowercase letter")

    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain an uppercase letter")

    if not re.search(r"[!?@#$%^&*()_+0-9\-=_~`\[\]{}|;:',.<>/?]", password) and not any(char.isdigit() for char in password):
        # The requirement specifies: one digit or punctuation character ([!? @#$ %^&* _ 0 -9])
        # Let's use a regex that covers digits and the specified special characters
        if not re.search(r"[0-9!@#$%^&*_\-]", password):
            errors.append("Password must contain a special character or a number")
    
    # Re-evaluating the specific requirement for the third check:
    # "one digit or punctuation character ([!? @#$ %^&* _ 0 -9])"
    # Let's refine the logic to match the exact error message and requirement.
    
    # Resetting error list for the specific third check to ensure accuracy
    # We need to check if it contains at least one digit OR one of the special characters
    has_digit = any(char.isdigit() for char in password)
    has_special = re.search(r"[!?@#$%^&*_\-]", password) is not None
    
    # Re-running the logic to ensure we don't double-add or miss based on the prompt's specific list
    # The prompt says: "Password must contain a special character or a number"
    # Let's rebuild the error collection to be precise.
    
    errors = []
    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")
    
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain a lowercase letter")
        
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain an uppercase letter")
        
    if not (re.search(r"[0-9]", password) or re.search(r"[!@#$%^&*_\-]", password)):
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"
    
    return errors