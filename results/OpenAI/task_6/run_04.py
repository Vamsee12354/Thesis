def IsValidPassword(password):
    errors = []
    if not isinstance(password, str) or not password:
        errors.append("Please fill the password")
        return errors
    length = len(password)
    if length < 12 or length > 72:
        errors.append("Length must be between 12 and 72 characters")
    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")
    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")
    if not any(c.isdigit() or c in "!@#$%^&*_?" for c in password):
        errors.append("Password must contain a special character or a number")
    if errors:
        return errors
    return "The password is valid"