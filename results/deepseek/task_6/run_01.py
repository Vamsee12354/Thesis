def is_valid_password(password):
    errors = []
    
    if not password:
        errors.append("Please fill the password")
        return errors
    
    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")
    
    has_lowercase = any(char.islower() for char in password)
    if not has_lowercase:
        errors.append("Password must contain a lowercase letter")
    
    has_uppercase = any(char.isupper() for char in password)
    if not has_uppercase:
        errors.append("Password must contain an uppercase letter")
    
    has_special_or_digit = any(char in '!?@#$%^&*_0-9' for char in password)
    if not has_special_or_digit:
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"

    return errors