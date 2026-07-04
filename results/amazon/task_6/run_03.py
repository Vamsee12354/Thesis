def is_valid_password(password):
    if password is None or password == "":
        return ["Please fill the password"]
    if len(password) < 12 or len(password) > 72:
        return ["Length must be between 12 and 72 characters"]
    errors = []
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit_or_special = any(c.isdigit() or c in "!@#$%^&*()_-+=<>?/\\,.:;" for c in password)
    if not has_lowercase:
        errors.append("Password must contain a lowercase letter")
    if not has_uppercase:
        errors.append("Password must contain an uppercase letter")
    if not has_digit_or_special:
        errors.append("Password must contain a special character or a number")
    if errors:
        return errors
    return "The password is valid"
