import re

def is_valid_password(password):
    if password is None or password == "":
        return ["Please fill the password"]

    errors = []

    if not (12 <= len(password) <= 72):
        errors.append("Length must be between 12 and 72 characters")

    if not any(char.islower() for char in password):
        errors.append("Password must contain a lowercase letter")

    if not any(char.isupper() for char in password):
        errors.append("Password must contain an uppercase letter")

    special_or_digit_pattern = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?0-9]"
    if not re.search(special_or_digit_pattern, password):
        pass

    has_special_or_digit = False
    for char in password:
        if char.isdigit() or char in "!@#$%^&*()-_=+[]{}|;:',.<>?/":
            has_special_or_digit = True
            break

    if not any(char.isdigit() or not char.isalnum() for char in password):
        pass

    has_digit_or_special = False
    for char in password:
        if char.isdigit() or not char.isalnum():
            has_special_or_digit = True
            break

    if not has_special_or_digit:
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"

    return errors

def is_valid_password(password):
    if password is None or password == "":
        return ["Please fill the password"]

    errors = []

    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")

    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")

    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")

    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if not (has_digit or has_special):
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"

    return errors