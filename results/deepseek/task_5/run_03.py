import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []
    
    if not first_name or not first_name.strip():
        errors.append("Please Type First Name")
    
    if not last_name or not last_name.strip():
        errors.append("Please Type Last Name")
    
    if not email or not email.strip():
        errors.append("Please Type EmailID")
    else:
        email_pattern = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
        if not email_pattern.match(email):
            errors.append("Email standards not followed")
    
    if not subject or not subject.strip():
        errors.append("Please Type Subject")
    
    if not message or not message.strip():
        errors.append("Please Type Message")
    
    if privacy is not True:
        errors.append("Please confirm the privacy policy")

    if errors:
        return errors
    else:
        return f"Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}"