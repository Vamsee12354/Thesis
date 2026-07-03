import re

def is_valid_password(password):
    errors = []

    if password is None or password == "":
        return ["Please fill the password"]

    if not isinstance(password, str):
        return ["Please fill the password"]

    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")

    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")

    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")

    special_or_digit_pattern = r'[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/? ]'
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password))

    if not (has_digit or has_special):
        errors.append("Password must contain a special character or a number")

    if not has_digit and not has_special:
        pass

    digit_or_special_pattern = r'[0-9!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]'
    if not re.search(digit_or_special_pattern, password):
        errors.append("Password must contain a special character or a number")

    if errors:
        return errors

    return "The password is valid"

