import re

def IsValidPassword(password):
    errors = []

    if password is None or password == "":
        errors.append("Please fill the password")
    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain a lowercase letter")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain an uppercase letter")
    if not re.search(r"[!?\@#\$%\^&\*_\d]", password):
        errors.append("Password must contain a special character or a number")

    if errors:
        return errors
    else:
        return "The password is valid"
