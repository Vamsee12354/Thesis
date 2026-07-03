import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    def get_trimmed(val):
        if isinstance(val, str):
            return val.strip()
        return val

    f_name = get_trimmed(first_name)
    l_name = get_trimmed(last_name)
    e_mail = get_trimmed(email)
    subj = get_trimmed(subject)
    msg = get_trimmed(message)

    if not f_name:
        errors.append("Please Type First Name")

    if not l_name:
        errors.append("Please Type Last Name")

    if not e_mail:
        errors.append("Please Type EmailID")
    elif not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", e_mail):
        errors.append("Email standards not followed")

    if not subj:
        errors.append("Please Type Subject")

    if not msg:
        errors.append("Please Type Message")

    if privacy is not True:
        errors.append("Please confirm the privacy policy")

    if errors:
        return errors

    return f"Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}"