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
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"

    return errors