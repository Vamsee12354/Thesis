import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    try:
        f_name = str(first_name).strip() if first_name is not None else ""
        if not f_name:
            errors.append("Please Type First Name")

        l_name = str(last_name).strip() if last_name is not None else ""
        if not l_name:
            errors.append("Please Type Last Name")

        email_str = str(email).strip() if email is not None else ""
        if not email_str:
            errors.append("Please Type EmailID")
        else:
            email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
            if not re.match(email_regex, email_str):
                errors.append("Email standards not followed")

        subj = str(subject).strip() if subject is not None else ""
        if not subj:
            errors.append("Please Type Subject")

        msg = str(message).strip() if message is not None else ""
        if not msg:
            errors.append("Please Type Message")

        if privacy is not True:
            errors.append("Please confirm the privacy policy")

    except Exception:
        return None

    if errors:
        return errors

    return f"Form is valid. Details:{f_name},{l_name},{email_str},{subj},{msg},{privacy}"