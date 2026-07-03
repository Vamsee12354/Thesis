import re

def is_valid_password(password):
    errors = []

    if password is None or password == "":
        return ["Please fill the password"]

    if not isinstance(password, str):
        return ["Please fill the password"]

    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")

    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")

    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")

    special_or_digit_pattern = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?0-9]"
    if not re.search(special_or_digit_pattern := r"[!@#$%^&* _0-9]", password):
        # The requirement specifies: [!? @#$ %^&* _ 0-9]
        # We check for digit or specific special characters
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*_" or c in " " for c in password)

        # Re-evaluating based on strict requirement: "one digit or punctuation character ([!? @#$ %^&* _ 0-9])"
        # Let's use a character class for the specific set provided in prompt
        if not re.search(r"[!? @#\$%^&* _0-9]", password):
             errors.append("Password must contain a special character or a number")
        else:
             pass # valid

    # Re-implementing the special/digit check to match the prompt's exact logic
    # The prompt lists: [!? @#$ %^&* _ 0-9]
    # We'll check if any character in password is in that set or is a digit
    pattern = r"[!?@#\$%^&* _0-9]"
    if not re.search(pattern, password):
        # The logic above might overlap with the length/case checks.
        # Let' |' refine based on exact requirement:
        pass

    # Let's restart the error collection cleanly to ensure no duplicates or missed logic
    errors = []

    if password is None or password == "":
        return ["Please fill the password"]

    if len(password) < 12 or len(password) > 72:
        errors.append("Length must be between 12 and 72 characters")

    if not any(c.islower() for c in password):
        errors.append("Password must contain a lowercase letter")

    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")

    # Requirements: "one digit or punctuation character ([!? @#$ %^&* _ 0-9])"
    # Note: The prompt says "special character or a number"
    # The set provided is [!? @#$ %^&* _ 0-9]
    pattern = r"[!?@#\$%^&* _0-9]"
    if not re.search(pattern, password):
        errors.append("Password must contain a special character or a number")

    if not errors:
        return "The password is valid"

    return errors