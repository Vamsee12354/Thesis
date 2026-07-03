import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    if not isinstance(first_name, str) or not first_name.strip():
        errors.append("Please Type First Name")

    if not isinstance(last_name, str) or not last_name.strip():
        errors.append("Please Type Last Name")

    email_str = ""
    if isinstance(email, str):
        email_str = email.strip()

    if not email_str:
        errors.append("Please Type EmailID")
    else:
        email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
        if not re.match(email_regex, email_str):
            errors.append("Email standards not followed")

    if not isinstance(subject, str) or not subject.strip():
        errors.append("Please Type Subject")

    if not isinstance(message, str) or not message.strip():
        errors.append("Please Type Message")

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
        str(privacy)
    ]

    return f"Form is valid. Details:{','.join(details)}"