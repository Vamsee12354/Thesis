def is_valid_password(password):
    if password is None or password == "":
        return ["Please fill the password"]
    if len(password) < 12 or len(password) > 72:
        return ["Length must be between 12 and 72 characters"]
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit_or_special = any(char.isdigit() or not char.isalpha() and not char.isspace() for char in password)
    errors = []
    if not has_lower:
        errors.append("Password must contain a lowercase letter")
    if not has_upper:
        errors.append("Password must contain an uppercase letter")
    if not has_digit_or_special:
        errors.append("Password must contain a special character or a number")
    if errors:
        return errors
    return "The password is valid"
