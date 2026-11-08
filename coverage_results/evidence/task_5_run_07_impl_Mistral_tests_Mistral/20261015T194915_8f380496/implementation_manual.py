def validate_form(first_name, last_name, email, subject, message, privacy):
    errors = []

    # Validate first_name
    if not first_name or not first_name.strip():
        errors.append("Please Type First Name")

    # Validate last_name
    if not last_name or not last_name.strip():
        errors.append("Please Type Last Name")

    # Validate email
    trimmed_email = email.strip() if email else ""
    if not trimmed_email:
        errors.append("Please Type EmailID")
    elif not trimmed_email or not trimmed_email.count('@') == 1 or not trimmed_email.count('.') >= 1:
        errors.append("Email standards not followed")

    # Validate subject
    if not subject or not subject.strip():
        errors.append("Please Type Subject")

    # Validate message
    if not message or not message.strip():
        errors.append("Please Type Message")

    # Validate privacy
    if privacy is not True:
        errors.append("Please confirm the privacy policy")

    if errors:
        return errors
    else:
        return f"Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}"