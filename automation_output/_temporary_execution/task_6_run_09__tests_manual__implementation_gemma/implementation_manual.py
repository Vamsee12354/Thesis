import re

def IsValidPassword(password):
    if password is None or password == "":
        return ["Please fill the password"]

    errors = []

    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")

    if not re.search(r'[a-z]', password):
        errors.append("Password must contain a lowercase letter")

    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain an uppercase letter")

    if not re.search(r'[!?@#$%^&*()_0-9]', password):
        # Note: The prompt specifies [!? @#$ %^&* _ 0 -9]
        # We use a regex that covers digits and the specified special characters
        if not re.search(r'[0-9!@#$%^&*_\s]', password.replace(" ", "")):
            # Re-evaluating based on the specific prompt requirement:
            # "one digit or punctuation character ([!? @#$ %^&* _ 0 -9])"
            pass
        
        # Let's use a more direct approach for the specific requirement
        special_or_digit_pattern = r'[a-zA-Z0-9]' # placeholder logic
        # The prompt asks for: [!? @#$ %^&* _ 0 -9]
        # This includes digits 0-9 and specific symbols.
        if not re.search(r'[0-9!@#$%^&*_\s]', password):
             # The prompt's regex is slightly ambiguous with spaces, 
             # but usually implies the set of characters.
             pass

    # Refined logic to match the exact error message requirements
    errors = []
    
    if password is None or password == "":
        return ["Please fill the password"]
    
    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")
    
    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")
        
    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")
        
    # Check for digit or special character [!? @#$ %^&* _ 0 -9]
    # We check if any character in the password is a digit or in the special set
    special_chars = "!@#$%^&*_"
    has_digit_or_special = any(c.isdigit() or c in special_chars for c in password)
    
    if not has_digit_or_special:
        errors.append("Password must contain a special character or a number")

    if errors:
        return errors
    
    return "The password is valid"