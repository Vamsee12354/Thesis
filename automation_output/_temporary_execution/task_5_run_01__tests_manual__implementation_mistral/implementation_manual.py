from typing import Any, Union
import re

def validate_form(first_name: str, last_name: str, email: str, subject: str, message: str, privacy: Any) -> Union[str, list[str]]:
    errors = []

    trimmed_first_name = first_name.strip()
    if not trimmed_first_name:
        errors.append("Please Type First Name")

    trimmed_last_name = last_name.strip()
    if not trimmed_last_name:
        errors.append("Please Type Last Name")

    trimmed_email = email.strip()
    if not trimmed_email:
        errors.append("Please Type EmailID")
    else:
        email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_pattern, trimmed_email):
            errors.append("Email standards not followed")

    trimmed_subject = subject.strip()
    if not trimmed_subject:
        errors.append("Please Type Subject")

    trimmed_message = message.strip()
    if not trimmed_message:
        errors.append("Please Type Message")

    if privacy is not True:
        errors.append("Please confirm the privacy policy")

    if errors:
        return errors
    else:
        return f"Form is valid. Details:{trimmed_first_name},{trimmed_last_name},{trimmed_email},{trimmed_subject},{trimmed_message},{privacy}"