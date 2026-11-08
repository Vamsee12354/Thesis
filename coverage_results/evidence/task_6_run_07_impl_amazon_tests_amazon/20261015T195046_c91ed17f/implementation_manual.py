def is_valid_password(password):
    if password is None or password == "":
        return ["Please fill the password"]
    errors = []
    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")
    if not any(char.islower() for char in password):
        errors.append("Password must contain a lowercase letter")
    if not any(char.isupper() for char in password):
        errors.append("Password must contain an uppercase letter")
    if not any(char.isdigit() or not char.isalpha() for char in password):
        errors.append("Password must contain a special character or a number")
    return errors if errors else "The password is valid"
