def is_valid_password(password):
    errors = []

    if not password:
        errors.append("Please fill the password")
        return errors

    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")

    has_lower = any(c.islower() for c in password)
    if not has_lower:
        errors.append("Password must contain a lowercase letter")

    has_upper = any(c.isupper() for c in password)
    if not has_upper:
        errors.append("Password must contain an uppercase letter")

    has_special_or_digit = any(c.isdigit() or not c.isalpha() for c in password)
    if not has_special_or_digit:
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"
    return errors