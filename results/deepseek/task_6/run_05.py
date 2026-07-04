def is_valid_password(password):
    errors = []
    
    if not password or len(password.strip()) == 0:
        errors.append("Please fill the password")
        return errors

    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit_or_special = any(not char.isalpha() for char in password)

    if not has_lower:
        errors.append("Password must contain a lowercase letter")
    if not has_upper:
        errors.append("Password must contain an uppercase letter")
    if not has_digit_or_special:
        errors.append("Password must contain a special character or a number")

    return "The password is valid" if not errors else errors
