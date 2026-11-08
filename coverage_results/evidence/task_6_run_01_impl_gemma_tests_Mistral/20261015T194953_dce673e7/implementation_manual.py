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

    if not re.search(r'[!?@#$%^&*()_+0-9\-=_~`\[\]{}|;:,.<>?/]', password) and not any(char.isdigit() for char in password):
        # The requirement specifies: one digit or punctuation character ([!? @#$ %^&* _ 0 -9])
        # Let's use a regex that covers digits and the specified special characters
        if not re.search(r'[0-9!@#$%^&*_\-]', password):
            errors.append("Password must contain a special character or a number")

    # Re-evaluating the specific regex requirement for the third rule:
    # "one digit or punctuation character ([!? @#$ %^&* _ 0 -9])"
    # Let's refine the check to match the prompt's specific character set requirement exactly.
    
    # Resetting error list for the third check to ensure precision
    if "Password must contain a special character or a number" in errors:
        pass # already handled
    else:
        # Check if it fails the specific requirement
        # The prompt lists: [!? @#$ %^&* _ 0 -9]
        # This translates to: digits or specific symbols
        pattern = r'[0-9!@#$%^&*_\-]'
        if not re.search(pattern, password):
            # If the previous check didn't catch it, we need to be careful.
            # Let's re-run the logic cleanly.
            pass

    # Clean implementation of the logic
    errors = []
    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")
    
    if not re.search(r'[a-z]', password):
        errors.append("Password must contain a lowercase letter")
        
    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain an uppercase letter")
        
    # The prompt requirement: "one digit or punctuation character ([!? @#$ %^&* _ 0 -9])"
    # We will check for any digit OR any of those specific characters.
    if not re.search(r'[0-9!@#$%^&*_\-]', password):
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"
    
    return errors