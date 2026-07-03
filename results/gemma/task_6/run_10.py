import re

def is_valid_password(password):
    errors = []

    if password is None or password == "":
        return ["Please fill the password"]

    if not isinstance(password, str):
        return ["Please fill the password"]

    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")

    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")

    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")

    special_or_digit_pattern = r'[a-zA-Z0-9]'
    # The prompt asks for: one digit or punctuation character ([!? @#$ %^&* _ 0 -9])
    # Re-evaluating requirement: "Password must contain a special character or a number"
    # Based on the regex provided in prompt: [!? @#$ %^&* _ 0 -9]
    # Effectively check if there is at least one digit OR one of those symbols.

    has_digit_or_special = any(c.isdigit() or c in "!?@#$%^&*_ " for c in password)

    # Refining based on the specific prompt constraint:
    # "one digit or punctuation character ([!? @#$ %^&* _ 0 -9])"
    # Note: The prompt's regex includes spaces and underscores.

    pattern = r'[0-9!?@#$ %^&*_]'
    if not re.search(pattern, password):
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"

    return errors