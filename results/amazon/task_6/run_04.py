def is_valid_password(password):
    if password is None or password == "":
        return ["Please fill the password"]
    
    errors = []
    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")
    
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit_or_special = any(c.isdigit() or not c.isalnum() for c in password)
    
    if not has_lowercase:
        errors.append("Password must contain a lowercase letter")
    if not has_uppercase:
        errors.append("Password must contain an uppercase letter")
    if not has_digit_or_special:
        errors.append("Password must contain a special character or a number")
    
    if errors:
        return errors
    else:
        return "The password is valid"
