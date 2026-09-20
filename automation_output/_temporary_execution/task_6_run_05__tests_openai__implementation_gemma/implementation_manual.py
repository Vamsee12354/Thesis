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

    if not re.search(r"[!?@#$%^&*()_+0-9\-=_~`\[\]{}|;':\",./<>?]", password) and not any(char.isdigit() for char in password):
        # The requirement specifies: one digit or punctuation character ([!? @#$ %^&* _ 0 -9])
        # Let's use a regex that covers digits and the specified special characters
        if not re.search(r"[!?@#$%^&* _0-9]", password):
            errors.append("Password must contain a special character or a number")

    # Re-evaluating the special character/number requirement based on the prompt's specific list
    # Prompt: "one digit or punctuation character ([!? @#$ %^&* _ 0 -9])"
    # Let's refine the check to be exact to the prompt's logic
    
    # Resetting error list for the specific character check to ensure accuracy
    # We need to check lowercase, uppercase, and (digit OR special)
    
    # Re-implementing logic cleanly
    errors = []
    
    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")
    
    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")
        
    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")
        
    # Check for digit or the specific special characters provided
    special_chars = "!?@#$%^&*_"
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_chars for c in password)
    
    if not (has_digit or has_special):
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"
    
    return errors