import re

def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    def check_empty(val, error_msg):
        if not isinstance(val, str) or not val.strip():
            errors.append(error_msg)
            return True
        return False

    if check_empty(first_name, "Please Type First Name"):
        pass
    elif not isinstance(first_name, str):
        errors.append("Please Type First Name")

    if check_empty(last_name, "Please Type Last Name"):
        pass
    elif not isinstance(last_name, str):
        errors.append("Please Type Last Name")

    email_str = str(email).strip() if email is not None else ""
    if not email_str:
        errors.append("Please Type EmailID")
    else:
        regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
        if not re.match(regex, email_str):
            errors.append("Email standards not followed")

    if check_empty(subject, "Please Type Subject"):
        pass
    elif not isinstance(subject, str):
        errors.append("Please Type Subject")

    if check_empty(message, "Please Type Message"):
        pass
    elif not isinstance(message, str):
        errors.append("Please Type Message")

    if privacy is not True:
        errors.append("Please confirm the privacy policy")

    if errors:
        return errors

    f_name = str(first_name).strip()
    l_name = str(last_name).strip()
    e_mail = email_str
    subj = str(subject).strip()
    msg = str(message).strip()
    priv = privacy

    return f"Form is valid. Details:{f_name},{l_name},{e_mail},{subj},{msg},{priv}"