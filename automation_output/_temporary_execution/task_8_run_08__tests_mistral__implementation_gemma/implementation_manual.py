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
        # Transliteration attempt using NFKD to decompose unicode
        # This handles many accented characters (e.g., 'é' -> 'e')
        # For CJK or other non-latin, we rely on a fallback approach
        # Since we cannot use external libraries like 'unidecode', 
        # we use unicodedata to normalize.
        normalized = unicodedata.normalize('NFKD', text)
        
        # Build a list of characters to keep or transform
        result_chars = []
        
        # We iterate through the normalized string
        # We want to keep alphanumeric, the separator, and ignored chars
        # Everything else becomes a space (to be replaced by separator later)
        
        temp_buffer = []
        for char in normalized:
            if char in ignore_set:
                temp_buffer.append(char)
            elif char.isalnum():
                temp_buffer.append(char)
            elif char.isspace():
                temp_buffer.append(" ")
            else:
                # Check if it's a non-spacing mark (part of decomposition)
                if unicodedata.category(char) != 'Mn':
                    temp_buffer.append(" ")
        
        processed_text = "".join(temp_buffer)
        
        if lowercase:
            processed_text = processed_text.lower()

        # Replace whitespace/multiple spaces with the separator
        # First, split by whitespace to handle multiple spaces and leading/trailing
        words = processed_text.split()
        
        # If we have ignored characters that are not alphanumeric, 
        # they might have been treated as separators if they weren't in the 'words' split.
        # However, the requirement says "alphanumerics and the configured separator".
        # Let's refine the logic:
        
        # 1. Create a string where everything not (alnum or in ignore) is a space
        # 2. Split by space
        # 3. Join with separator
        
        # Re-evaluating the "你好" example: "你好" -> "ni-hao"
        # Without 'unidecode', true transliteration of CJK is impossible in pure stdlib.
        # However, the prompt implies we should try. 
        # Since I cannot use external libs, I will implement the logic as best as possible 
        # with unicodedata.
        
        # Let's try a more robust approach for the "words"
        # We'll treat any sequence of (alnum or ignored) as a word.
        
        pattern = r'[^a-zA-Z0-9' + re.escape("".join(ignore_set)) + r']+'
        # Note: this regex approach is tricky with unicode.
        
        # Let's stick to the character-by-character logic
        final_parts = []
        current_word = []
        
        for char in processed_text:
            if char.isalnum() or char in ignore_set:
                current_word.append(char)
            else:
                if current_word:
                    final_parts.append("".join(current_word))
                    current_word = []
        if current_word:
            final_parts.append("".join(current_word))
            
        slug = separator.join(final_parts)
        
        if not slug:
            return None

        # Truncation logic: "truncating without breaking words"
        if truncate is not None and truncate > 0:
            if len(slug) > truncate:
                # Find the last separator within the limit
                truncated_slug = slug[:truncate]
                last_sep = truncated_slug.rfind(separator)
                
                # If separator is empty string, rfind returns -1
                if separator == "":
                    slug = truncated_slug
                elif last_sep != -1:
                    slug = truncated_slug[:last_sep]
                else:
                    # If no separator found, we might have to truncate strictly 
                    # or return None if it breaks the word. 
                    # The prompt says "without breaking words". 
                    # If the first word is longer than truncate, we return None or empty.
                    # But usually, in slugify, if truncate is 10 and word is 15, 
                    # and no separator exists, we return None or the truncated part.
                    # Given "Call me maybe" (14 chars) -> "call-me" (7 chars) with truncate 10.
                    # "call-me" is the longest word-complete part.
                    slug = "" # Will return None below
                
                # If slug became empty due to truncation logic
                if not slug and truncate > 0:
                    # Check if the first word itself fits
                    first_word = final_parts[0] if final_parts else ""
                    if len(first_word) <= truncate:
                        slug = first_word
                    else:
                        return None

        if not slug:
            return None
            
        return slug

    except Exception:
        return None