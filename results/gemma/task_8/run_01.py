import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    try:
        text.encode('utf-8').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return None

    if ignore is None:
        ignore_chars = set()
    elif isinstance(ignore, str):
        ignore_chars = set(ignore)
    else:
        ignore_chars = set("".join(ignore))

    def transliterate(s):
        normalized = unicodedata.normalize('NFKD', s)
        return "".join([c for c in normalized if not unicodedata.combining(c)])

    # Transliteration/Normalization
    text = transliterate(text)

    # Convert to lowercase if requested
    if lowercase:
        text = text.lower()

    # Build a pattern of allowed characters
    # Allowed: Alphanumeric, separator, and characters in ignore
    # We first handle the characters that are NOT ignored and NOT alphanumeric/separator

    # Step 1: Identify which characters to keep
    # We will iterate through the string and build a list of tokens
    # Tokens are sequences of alphanumeric characters or ignored characters

    result_chars = []

    # Clean up text by replacing non-alphanumeric and non-ignored with spaces
    # But we must treat the separator as a special case

    # Replace punctuation/symbols with space, but keep ignore chars
    processed_chars = []
    for char in text:
        if char.isalnum() or char in ignore_chars or char == separator:
            processed_chars.append(char)
        elif char in ignore_chars:
            processed_chars.append(char)
        else:
            processed_chars.append(' ')

    temp_text = "".join(processed_chars)

    # Step 2: Split by whitespace to get words
    raw_words = temp_text.split()

    # Step 3: Clean words (remove trailing/leading separators from words)
    cleaned_words = []
    for word in raw_words:
        # Remove leading/trailing separators from word
        w = word.strip(separator)
        if w:
            cleaned_words.append(w)

    if not cleaned_words:
        return None

    # Reconstruct using separator
    full_slug = separator.join(cleaned_words)

    # Step 4: Truncation logic (without breaking words)
    if truncate is not None and truncate > 0:
        if len(full_slug) <= truncate:
            pass
        else:
            # Find the last separator or space within the limit
            truncated_text = full_slug[:truncate]
            last_sep = truncated_text.rfind(separator)

            if last_sep!= -1:
                full_slug = truncated_text[:last_sep].rstrip(separator)
            else:
                # If no separator exists in the limit, the word is too long
                # The requirement says "truncating without breaking words"
                # If the first word is longer than truncate, we might return None
                # or an empty string. Based on "may eliminate all words", we return None.
                return None

    if not full_slug:
        return None

    return full_slug