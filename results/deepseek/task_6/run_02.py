import re

def is_valid_password(password):
    if not password:
        return ["Please fill the password"]

    errors = []

    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")

    if not re.search(r'[a-z]', password):
        errors.append("Password must contain a lowercase letter")

    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain an uppercase letter")

    if not re.search(r'[\d!?@#$%^&*_]', password):
        errors.append("Password must contain a special character or a number")

    return "The password is valid" if not errors else errors