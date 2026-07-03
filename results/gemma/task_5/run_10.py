import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    def clean(val):
        if isinstance(val, str):
            return val.strip()
        return val

    f_name = clean(first_name)
    l_name = clean(last_name)
    e_mail = clean(email)
    subj = clean(subject)
    msg = clean(message)

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

    details = [
        str(first_name),
        str(last_name),
        str(email),
        str(subject),
        str(message),
        str(privacy)
    ]

    return f"Form is valid. Details:{','.join(details)}"