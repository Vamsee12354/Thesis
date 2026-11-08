import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []
    if not first_name.strip():
        errors.append("Please Type First Name")
    if not last_name.strip():
        errors.append("Please Type Last Name")
    if not email.strip():
        errors.append("Please Type EmailID")
    elif not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email.strip()):
        errors.append("Email standards not followed")
    if not subject.strip():
        errors.append("Please Type Subject")
    if not message.strip():
        errors.append("Please Type Message")
    if not privacy:
        errors.append("Please confirm the privacy policy")
    return errors if errors else f"Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}"
