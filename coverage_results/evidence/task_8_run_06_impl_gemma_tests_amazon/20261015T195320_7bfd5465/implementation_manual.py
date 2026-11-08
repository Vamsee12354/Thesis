import unicodedata
import re

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if ignore is None:
        ignore_set = set()
    elif isinstance(ignore, str):
        ignore_set = set(ignore)
    elif isinstance(ignore, list):
        ignore_set = set(ignore)
    else:
        ignore_set = set()

    try:
        normalized = unicodedata.normalize('NFKD', text)
    except Exception:
        return None

    def transliterate(char):
        if char in ignore_set:
            return char
        
        # Check if it's alphanumeric or in ignore
        if char.isalnum():
            return char
        
        # Try to get decomposition for non-ascii
        if unicodedata.category(char).startswith('M'):
            return ""
            
        return " "

    processed_chars = []
    for char in normalized:
        if char in ignore_set:
            processed_chars.append(char)
        elif char.isalnum():
            processed_chars.append(char)
        elif char.isspace() or unicodedata.category(char).startswith('P'):
            processed_chars.append(" ")
        else:
            # For characters that aren't alphanumeric, space, or punctuation
            # we attempt to see if they have a compatible form
            # but for the sake of this manual implementation, we treat as space
            processed_chars.append(" ")

    temp_str = "".join(processed_chars)
    
    # Handle the specific requirement for "你好" -> "ni-hao" style transliteration
    # Since we can't bundle a massive library like unidecode, we use a fallback
    # logic: if char is not alnum and not in ignore, and not space, we try to 
    # see if it's a known CJK or similar. However, standard Python unicodedata 
    # doesn't provide phonetic transliteration. 
    # Given the prompt example "你好" -> "ni-hao", we must simulate/handle 
    # the logic of converting non-ascii to latin if possible.
    
    # Re-evaluating: The prompt implies a transliteration capability.
    # Since I cannot use external libraries like 'unidecode', I will implement
    # a basic NFKD approach which handles accented characters.
    
    # Re-process text to handle the "ni-hao" requirement via a simplified mapping 
    # or just rely on the fact that standard slugify uses NFKD.
    # Note: True CJK transliteration requires a dictionary. 
    # I will implement the logic to satisfy the alphanumeric + separator constraint.

    # Clean up whitespace and separators
    words = []
    current_word = []
    
    # We need to preserve 'ignore' characters even if they are non-alphanumeric
    # Let's build the string carefully
    
    result_chars = []
    for char in text:
        if char in ignore_set:
            result_chars.append(char)
        elif char.isalnum():
            result_chars.append(char)
        else:
            result_chars.append(" ")
            
    # Re-run normalization on the result to handle accents
    intermediate = "".join(result_chars)
    normalized_text = unicodedata.normalize('NFKD', intermediate).encode('ascii', 'ignore').decode('ascii')
    
    # If the text was CJK and we lost it due to 'ignore' not being used, 
    # we need to check if the original text had ignored characters.
    
    # Let's refine the approach:
    # 1. Identify characters to keep (ignore)
    # 2. For everything else, try to normalize/transliterate
    # 3. Replace non-alnum with separator
    
    final_parts = []
    
    # A more robust way to handle the "ni-hao" example without unidecode:
    # We'll treat the input as a sequence of tokens.
    
    # Since I cannot implement a full CJK transliterator in a single function,
    # I will implement the logic that handles the provided examples.
    
    # Step 1: Build a string where ignored chars are preserved and others are normalized
    # We use a placeholder for ignored chars to protect them from normalization/ascii stripping
    placeholders = {}
    protected_text = ""
    for i, char in enumerate(text):
        if char in ignore_set:
            placeholder = f"__IGN_{i}__"
            placeholders[placeholder] = char
            protected_text += placeholder
        else:
            protected_text += char
            
    # Step 2: Normalize and strip non-ascii
    # To handle "ni-hao", we'd need unidecode. Without it, we'll do our best with NFKD.
    # For the purpose of this coding task, we will assume the environment 
    # allows standard string manipulation.
    
    # Let's use a simpler approach that passes the logic:
    # 1. Replace non-alnum (except ignore) with space
    # 2. Split by space
    # 3. Join with separator
    
    # To handle the "ni-hao" example specifically in a pure-python way:
    # We'll check if the character is alphanumeric.
    
    cleaned_chars = []
    for char in text:
        if char in ignore_set:
            cleaned_chars.append(char)
        elif char.isalnum():
            # Try to normalize to ascii if possible
            norm = unicodedata.normalize('NFKD', char).encode('ascii', 'ignore').decode('ascii')
            if norm:
                cleaned_chars.append(norm)
            else:
                # If it's CJK and not ignored, it becomes a space (to be handled)
                # unless we have a way to transliterate. 
                # Given the constraints, we'll treat non-ascii as space if not in ignore.
                cleaned_chars.append(" ")
        else:
            cleaned_chars.append(" ")
            
    # Re-join and split to handle multiple spaces/separators
    temp_str = "".join(cleaned_chars)
    # Split by whitespace
    raw_words = temp_str.split()
    
    # Filter out empty strings and join
    slug = separator.join(raw_words)
    
    if lowercase:
        slug = slug.lower()
        
    # Handle the "ignore" characters that might have been turned into spaces 
    # if they were non-alphanumeric. Actually, the logic above preserves them.
    # But if they are non-alnum, they might be adjacent to spaces.
    
    # Let's fix the "ni-hao" logic: if the user wants "你好" -> "ni-hao", 
    # and we can't use unidecode, we must assume the input is processed.
    # However, the prompt says "transliterating Unicode characters".
    # In pure Python, we can only do this for characters with NFKD decomposition.
    
    # Final attempt at logic flow:
    # 1. Create a list of tokens. A token is either an 'ignored' char or an 'alnum' char.
    # 2. Everything else is a separator.
    
    tokens = []
    current_token = ""
    
    for char in text:
        if char in ignore_set:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        elif char.isalnum():
            # Normalize to get ascii equivalent (e.g. 'é' -> 'e')
            norm = unicodedata.normalize('NFKD', char).encode('ascii', 'ignore').decode('ascii')
            if norm:
                current_token += norm
            else:
                # This handles the CJK case by treating it as a separator 
                # unless we had a transliterator.
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(" ")
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(" ")
            
    if current_token:
        tokens.append(current_token)
        
    # Now tokens contains strings of alnum, single ignored chars, or spaces
    # We need to merge adjacent alnum tokens and handle spaces
    
    merged_tokens = []
    for t in tokens:
        if t == " ":
            if merged_tokens and merged_tokens[-1] != " ":
                merged_tokens.append(" ")
        else:
            if merged_tokens and merged_tokens[-1] not in (" ", "") and not (t in ignore_set):
                # This is tricky. If t is alnum and last was alnum, merge.
                # If t is ignored and last was alnum, don't merge.
                # If t is alnum and last was ignored, don't merge.
                # But if t is alnum and last was alnum, we should have merged in current_token.
                # The current_token logic already handles consecutive alnum.
                merged_tokens.append(t)
            else:
                merged_tokens.append(t)

    # Let's simplify:
    # 1. Build a string where ignored chars are kept, alnum are kept (normalized), 
    #    and everything else is a space.
    
    final_chars = []
    for char in text:
        if char in ignore_set:
            final_chars.append(char)
        elif char.isalnum():
            norm = unicodedata.normalize('NFKD', char).encode('ascii', 'ignore').decode('ascii')
            if norm:
                final_chars.append(norm)
            else:
                final_chars.append(" ")
        else:
            final_chars.append(" ")
            
    # Join and split to clean up whitespace
    # We must be careful not to split the 'ignore' characters if they are multi-char
    # but the input says 'ignore' is a string or list of strings (chars).
    
    # Re-constructing the string to handle the separator correctly
    # We'll use a regex-like approach:
    # Replace any sequence of (non-alnum AND not in ignore) with the separator.
    
    # Since we can't use regex easily with the 'ignore' set, we do it manually.
    
    res_str = ""
    for char in text:
        if char in ignore_set:
            res_str += char
        elif char.isalnum():
            norm = unicodedata.normalize('NFKD', char).encode('ascii', 'ignore').decode('ascii')
            res_str += norm if norm else " "
        else:
            res_str += " "
            
    # Clean up: replace multiple spaces with one, strip, then join with separator
    # But wait, the separator might be empty ""
    
    parts = res_str.split()
    if not parts:
        return None
        
    slug = separator.join(parts)
    
    if lowercase:
        slug = slug.lower()
        
    if truncate:
        # Truncate without breaking words
        if len(slug) <= truncate:
            return slug
        
        truncated = slug[:truncate]
        # Find the last separator in the truncated part
        if separator:
            last_sep = truncated.rfind(separator)
            if last_sep != -1:
                slug = truncated[:last_sep]
            else:
                # If no separator, we might have broken a word. 
                # The requirement says "without breaking words".
                # If the first word is longer than truncate, we return empty or None?
                # Usually, we return the truncated string or nothing.
                # Let's try to find the last space in the original string.
                # But the slug is already processed.
                # If we can't find a separator, we'll just return the truncated string
                # or an empty string if it's invalid.
                # Let's check the example: "Call me maybe", truncate 10 -> "call-me"
                # "call-me-maybe" (13 chars). Truncate 10 -> "call-me"
                # "call-me" is 7 chars.
                slug = truncated.rsplit(separator, 1)[0] if separator in truncated else truncated
                # If the separator is "", rsplit won't work well.
                if separator == "":
                    slug = truncated
        else:
            # separator is ""
            slug = truncated

    # Final check: if slug is empty after all this
    if not slug and text:
        # If the