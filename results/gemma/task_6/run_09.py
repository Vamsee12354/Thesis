import re

def is_valid_password(password):
    errors = []

    if password is None or password == "":
        errors.append("Please fill the password")
        return errors

    if not isinstance(password, str):
        return ["Invalid input type"]

    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")

    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")

    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")

    pattern = r'[!?@#$%^&*()_+=\-\[\]{};\':"\\|,.<>\/?0-9]'
    if not re.search(pattern, password):
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"

    return errors