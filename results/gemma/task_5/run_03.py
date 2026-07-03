import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    try:
        f_name = str(first_name).strip() if first_name is not None else ""
        l_name = str(last_name).strip() if last_name is not None else ""
        e_mail = str(email).strip() if email is not None else ""
        subj = str(subject).strip() if subject is not None else ""
        msg = str(message).strip() if message is not None else ""
        priv = privacy

        if not f_name:
            errors.append("Please Type First Name")

        if not l_name:
            errors.append("Please Type Last Name")

        if not e_mail:
            errors.append("Please Type EmailID")
        else:
            email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
            if not re.match(email_regex, e_mail):
                errors.append("Email standards not followed")

        if not subj:
            errors.append("Please Type Subject")

        if not msg:
            errors.append("Please Type Message")

        if priv is not True:
            errors.append("Please confirm the privacy policy")

        if errors:
            return errors

        details = f"{f_name},{l_name},{e_mail},{subj},{msg},{privacy}"
        return f"Form is valid. Details:{details}"

    except Exception:
        return None