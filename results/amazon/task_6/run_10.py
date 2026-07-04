def is_valid_password(password):
    if password is None or password == "":
        return ["Please fill the password"]
    
    errors = []
    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")
    
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit_or_special = any(char.isdigit() or not char.isalnum() for char in password)
    
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
