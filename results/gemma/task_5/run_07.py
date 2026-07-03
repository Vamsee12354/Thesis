import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    def get_trimmed(val):
        if val is None:
            return ""
        return str(val).strip()

    t_first_name = get_trimmed(first_name)
    t_last_name = get_trimmed(last_name)
    t_email = get_trimmed(email)
    t_subject = get_trimmed(subject)
    t_message = get_trimmed(message)

    if not t_first_name:
        errors.append("Please Type First Name")

    if not t_last_name:
        errors.append("Please Type Last Name")

    if not t_email:
        errors.append("Please Type EmailID")
    else:
        email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
        if not re.match(email_regex, t_email):
            errors.append("Email standards not followed")

    if not t_subject:
        errors.append("Please Type Subject")

    if not t_message:
        errors.append("Please Type Message")

    if privacy is not True:
        errors.append("Please confirm the privacy policy")

    if errors:
        return errors

    return f"Form is valid. Details:{t_first_name},{t_last_name},{t_email},{t_subject},{t_message},{privacy}"