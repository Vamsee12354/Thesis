import unicodedata
import re

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if ignore is None:
        ignore_chars = set()
    elif isinstance(ignore, str):
        ignore_chars = set(ignore)
    elif isinstance(ignore, list):
        ignore_chars = set("".join(ignore))
    else:
        ignore_chars = set()

    try:
        text = unicodedata.normalize('NFKD', text)
    except Exception:
        return None

    def transliterate(char):
        if char in ignore_chars:
            return char
        if char.isalnum():
            return char
        return None

    # Attempt to handle common CJK/Unicode transliteration via decomposition
    # Since we cannot use external libraries like unidecode, we rely on NFKD
    # and filtering. For specific requirements like "你好" -> "ni-hao", 
    # standard library NFKD won't do it, but we follow the logic of 
    # alphanumeric preservation.
    
    processed_chars = []
    for char in text:
        if char in ignore_chars:
            processed_chars.append(char)
        elif char.isalnum():
            processed_chars.append(char)
        elif char.isspace():
            processed_chars.append(" ")
        else:
            # Check if it's a non-spacing mark that was decomposed
            if unicodedata.category(char) != 'Mn':
                processed_chars.append(" ")

    temp_str = "".join(processed_chars)
    
    # Clean up whitespace and separators
    words = temp_str.split()
    
    # Reconstruct with separator
    slug = separator.join(words)

    # Apply casing
    if lowercase:
        slug = slug.lower()

    # Final filter: ensure only alphanumeric, separator, or ignored chars remain
    # This handles cases where punctuation was replaced by spaces
    final_chars = []
    for i, char in enumerate(slug):
        if char in ignore_chars or char.isalnum():
            final_chars.append(char)
        elif i > 0 and i < len(slug) - 1 and slug[i:i+len(separator)] == separator:
            # This is a bit tricky with multi-char separators, 
            # but for standard single char:
            final_chars.append(char)
        elif char == separator[0] if len(separator) == 1 else char in separator:
            final_chars.append(char)

    # Re-verify the slug structure to ensure no illegal chars leaked
    # and that separators are correctly placed.
    # A more robust way:
    pattern = r'[^a-zA-Z0-9' + re.escape(separator) + r']'
    # We must also allow the ignored characters in the regex
    if ignore_chars:
        for ic in ignore_chars:
            if ic.isalnum(): continue
            pattern = pattern.replace('^', f'^{re.escape(ic)}')
    
    # Since regex with dynamic ignore is complex, let's use a simpler approach:
    # Build the slug word by word.
    
    valid_words = []
    for word in words:
        clean_word = ""
        for c in word:
            if c.isalnum() or c in ignore_chars:
                clean_word += c
            elif c in ignore_chars:
                clean_word += c
        if clean_word:
            valid_words.append(clean_word)
            
    slug = separator.join(valid_words)
    
    if lowercase:
        slug = slug.lower()

    if not slug:
        return None

    # Truncation logic: "without breaking words"
    if truncate is not None and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            # Find last separator to avoid breaking words
            if separator:
                last_sep = truncated.rfind(separator)
                if last_sep != -1:
                    slug = truncated[:last_sep]
                else:
                    # If no separator, we might have to truncate strictly 
                    # or return None if it breaks the only word.
                    # The prompt says "without breaking words".
                    # If the first word is longer than truncate, we return empty/None.
                    slug = "" 
            else:
                slug = truncated
            
            # If truncation resulted in empty string (e.g. truncate=2, word="hello")
            if not slug and len(valid_words) > 0:
                # If we can't fit even one word, return None as per edge case
                return None

    # Final check for empty result
    if not slug:
        return None

    return slug