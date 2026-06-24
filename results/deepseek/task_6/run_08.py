def is_valid_password(password):
    errors = []
    
    if not password or not isinstance(password, str):
        errors.append("Please fill the password")
        return errors
    
    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")
    
    has_lowercase = any(c.islower() for c in password)
    if not has_lowercase:
        errors.append("Password must contain a lowercase letter")
    
    has_uppercase = any(c.isupper() for c in password)
    if not has_uppercase:
        errors.append("Password must contain an uppercase letter")
    
    has_special_or_digit = any(not c.isalpha() for c in password)
    if not has_special_or_digit:
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"
    else:
        return errors