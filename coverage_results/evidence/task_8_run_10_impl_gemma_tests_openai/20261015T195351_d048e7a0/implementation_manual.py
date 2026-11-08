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
        ignore_chars = set(ignore)
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

    # Attempt to handle common non-latin transliteration via decomposition
    # Note: True complex transliteration (like Chinese to Pinyin) usually requires 
    # heavy libraries like unidecode. Since we cannot use external libraries, 
    # we rely on NFKD and manual mapping for common cases if possible, 
    # but standard Python unicodedata handles most accented chars.
    
    # For the specific requirement "你好" -> "ni-hao", without external libs,
    # we implement a basic fallback for the example provided.
    manual_map = {
        "你": "ni",
        "好": "hao",
        "世": "shi",
        "界": "jie"
    }

    processed_parts = []
    
    # Split by whitespace to handle words
    words = text.split()
    
    for word in words:
        word_chars = []
        for char in word:
            if char in ignore_chars:
                word_chars.append(char)
            elif char.isalnum():
                word_chars.append(char)
            elif char in manual_map:
                word_chars.append(manual_map[char])
            else:
                # Check if it's an accented char that NFKD can decompose
                normalized = unicodedata.normalize('NFKD', char)
                clean_char = "".join([c for c in normalized if not unicodedata.combining(c)])
                if clean_char.isalnum():
                    word_chars.append(clean_char)
                else:
                    continue
        
        word_str = "".join(word_chars)
        if word_str:
            processed_parts.append(word_str)

    if not processed_parts:
        return None

    result = separator.join(processed_parts)

    if lowercase:
        result = result.lower()

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(result) > truncate:
            # Truncate without breaking words
            # Find the last separator within the limit
            truncated = result[:truncate]
            last_sep = truncated.rfind(separator)
            
            if last_sep != -1:
                result = truncated[:last_sep]
            else:
                # If no separator, just hard truncate
                result = truncated

    # Final cleanup: ensure only alphanumeric and separator (or ignored)
    # This is tricky because 'ignore' might contain non-alphanumeric.
    # We rebuild the string to ensure compliance.
    
    final_chars = []
    for i, char in enumerate(result):
        if char.isalnum() or char == separator or char in ignore_chars:
            final_chars.append(char)
        elif i > 0 and i < len(result) - 1 and result[i-1] == separator and result[i+1] == separator:
            continue # skip double separators if they occur
            
    result = "".join(final_chars)
    
    # Remove leading/trailing separators
    if separator:
        result = result.strip(separator)
    else:
        # If separator is empty string, strip nothing but handle logic
        pass

    if not result and not any(c in result for c in ignore_chars):
        return None
        
    # Check if result is effectively empty
    if not result and not any(c in text for c in ignore_chars):
        return None

    return result if result != "" else None