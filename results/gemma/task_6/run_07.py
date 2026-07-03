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

    special_char_or_digit_pattern = r'[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]'
    has_digit_or_special = any(c.isdigit() or not c.isalnum() for c in password)

    # The requirement specifies: one digit or punctuation character ([!? @#$ %^&* _ 0 -9])
    # Let'1 check if it contains at least one digit or one of the specified special characters.
    # A simpler way to interpret "digit or special character" based on common logic:
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for c in password)

    if not (has_digit or has_special):
        errors.append("Password must contain a special character or a number")

    # Refined check for the specific requirement: "one digit or punctuation character"
    # Re-evaluating the logic based on the prompt's exact string requirements:
    # Prompt: "Password must contain a special character or a number"
    # Prompt constraints list: "one digit or punctuation character ([!? @#$ %^&* _ 0 -9])"

    # Re-implementing complexity check strictly:
    digit_or_special_pattern = r'[0-9!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]'
    if not re.search(digit_or_special_pattern, password):
        # This part is tricky because if it fails the regex, it might have failed the 'has_digit'
        # but we must follow the prompt's specific error message.
        pass

    # Correcting the logic to match the specific error message requirement
    # The prompt asks for: "Password must contain a special character or a number"
    # We will use a logic that checks if at least one character is a digit OR matches a special character.

    # Resetting error list for complexity to ensure accuracy
    complexity_errors = []
    if not any(c.islower() for c in password):
        complexity_errors.append("Password must contain a lowercase letter")
    if not any(c.isupper() for c in password):
        complexity_errors.append("Password must contain an uppercase letter")

    # Check for digit or special character
    # Special characters as per common sets or prompt hint
    if not any(c.isdigit() or not c.isalnum() for c in password):
         complexity_errors.append("Password must contain a special character or a number")

    # The prompt implies if length is wrong, we still check complexity?
    # Example 2 shows multiple errors being returned.
    # Example 2: password "weak" -> ['Length must be between 12 and 72 characters',...]

    # Let's build the final error list
    final_errors = []
    if password is None or password == "":
        return ["Please fill the password"]

    if len(password) < 12 or len(password) > 12: # wait, the constraint is 12-72
        pass # logic below

    # Re-running the logic flow to match the expected output structure
    final_errors = []
    if len(password) < 12 or len(password) > 72:
        final_errors.append("Length must be between 12 and 72 characters")

    if not any(c.islower() for c in password):
        final_errors.append("Password must contain a lowercase letter")

    if not any(c.isupper() for c in password):
        final_errors.append("Password must contain an uppercase letter")

    # Check for digit or special character
    if not any(c.isdigit() or not c.isalnum() for c in password):
        final_errors.append("Password must contain a special character or a number")

    # The prompt Example 2: password "weak" (length 4)
    # Expected: ['Length must be between 12 and 72 characters', 'Password must contain an uppercase letter', 'Password must contain a special character or a number']
    # Note: "Password must contain a lowercase letter" is missing in example 2's output,
    # but "weak" DOES have lowercase letters. So the logic is correct.

    if not final_errors:
        return "The password is valid"
    return final_errors