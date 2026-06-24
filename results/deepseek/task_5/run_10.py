import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []
    
    if not isinstance(first_name, str) or not first_name.strip():
        errors.append("Please Type First Name")
    
    if not isinstance(last_name, str) or not last_name.strip():
        errors.append("Please Type Last Name")
    
    if not isinstance(email, str) or not email.strip():
        errors.append("Please Type EmailID")
    else:
        email_pattern = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
        if not email_pattern.match(email.strip()):
            errors.append("Email standards not followed")
    
    if not isinstance(subject, str) or not subject.strip():
        errors.append("Please Type Subject")
    
    if not isinstance(message, str) or not message.strip():
        errors.append("Please Type Message")
    
    if not isinstance(privacy, bool) or not privacy:
        errors.append("Please confirm the privacy policy")
    
    if errors:
        return errors
    else:
        return f"Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}"