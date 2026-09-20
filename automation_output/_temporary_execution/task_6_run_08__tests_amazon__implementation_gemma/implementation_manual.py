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

    if not re.search(r'[!?@#$%^&*()_+0-9\-=_]', password) and not any(c.isdigit() or c in "!@#$%^&*()_+-=" for c in password):
        # The requirement specifies: one digit or punctuation character ([!? @#$ %^&* _ 0 -9])
        # Let's use a regex that covers digits and the specified special characters
        if not re.search(r'[0-9!@#$%^&*()_+=\-]', password):
            errors.append("Password must contain a special character or a number")
    
    # Re-evaluating the specific regex requirement for the third rule:
    # "one digit or punctuation character ([!? @#$ %^&* _ 0 -9])"
    # Let's refine the logic to match the prompt's exact error message and character set.
    
    # Resetting error list for the third rule to ensure precision
    # We need to check if the password contains at least one digit OR one of the special characters.
    
    # Re-running logic for clarity
    errors = []
    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")
    
    if not re.search(r'[a-z]', password):
        errors.append("Password must contain a lowercase letter")
        
    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain an uppercase letter")
        
    # The prompt defines the set as: [!? @#$ %^&* _ 0 -9]
    # This translates to digits 0-9 and characters: ! ? @ # $ % ^ & * _ (and space/dash implied by the range)
    # However, standard interpretation of "digit or punctuation" in these tasks is:
    if not re.search(r'[0-9!@#$%^&*()_+\-]', password):
        # Note: The prompt's character set is slightly messy in text, 
        # but the logic is: digit OR special char.
        # Let's use a robust check for digit or common special chars.
        pass

    # Let's rewrite the logic cleanly to match the exact expected behavior.
    
    errors = []
    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")
    
    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")
        
    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")
        
    # Check for digit or special character
    # Special characters mentioned: ! ? @ # $ % ^ & * _
    special_chars = "!@#$%^&*_"
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_chars for c in password)
    
    if not (has_digit or has_special):
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"
    
    return errors