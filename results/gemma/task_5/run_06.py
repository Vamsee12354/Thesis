import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    def check_empty(val, error_msg):
        if not isinstance(val, str) or not val.strip():
            errors.append(error_msg)
            return True
        return False

    # First Name
    if check_empty(first_name, "Please Type First Name"):
        pass

    # Last Name
    if check_empty(last_name, "Please Type Last Name"):
        pass

    # Email
    email_str = str(email).strip() if email is not None else ""
    if not email_str:
        errors.append("Please Type EmailID")
    else:
        email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
        if not re.match(email_regex, email_str):
            errors.append("Email standards not followed")

    # Subject
    if check_empty(subject, "Please Type Subject"):
        pass

    # Message
    if check_empty(message, "Please Type Message"):
        pass

    # Privacy
    if privacy is not True:
        errors.append("Please confirm the privacy policy")

    if errors:
        return errors

    details = [
        str(first_name).strip(),
        str(last_name).strip(),
        email_str,
        str(subject).strip(),
        str(message).strip(),
        privacy
    ]

    return f"Form is valid. Details:{','.join(details)}"