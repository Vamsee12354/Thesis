import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    def clean(val):
        if isinstance(val, str):
            return val.strip()
        return val

    c_first_name = clean(first_name)
    c_last_name = clean(last_name)
    c_email = clean(email)
    c_subject = clean(subject)
    c_message = clean(message)

    if not c_first_name:
        errors.append("Please Type First Name")

    if not c_last_name:
        errors.append("Please Type Last Name")

    if not c_email:
        errors.append("Please Type EmailID")
    elif not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", c_email):
        errors.append("Email standards not followed")

    if not c_subject:
        errors.append("Please Type Subject")

    if not c_message:
        errors.append("Please Type Message")

    if privacy is not True:
        errors.append("Please confirm the privacy policy")

    if errors:
        return errors

    return f"Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}"