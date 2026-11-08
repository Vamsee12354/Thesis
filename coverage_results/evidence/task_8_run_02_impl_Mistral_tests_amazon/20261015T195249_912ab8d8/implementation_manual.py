def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text:
        return None

    if ignore is not None:
        if isinstance(ignore, str):
            ignore = [ignore]
        ignore_set = set(ignore)
    else:
        ignore_set = set()

    normalized = []
    for char in text:
        if char in ignore_set:
            normalized.append(char)
        else:
            try:
                normalized_char = char.encode('ascii', 'ignore').decode('ascii')
                if normalized_char:
                    normalized.append(normalized_char)
            except (UnicodeEncodeError, UnicodeDecodeError):
                continue

    if not normalized:
        return None

    cleaned = []
    for char in normalized:
        if char.isalnum() or char in ignore_set:
            cleaned.append(char)
        else:
            cleaned.append(' ')

    slug = ''.join(cleaned)
    slug = ' '.join(slug.split())

    if lowercase:
        slug = slug.lower()

    if separator:
        slug = slug.replace(' ', separator)
    else:
        slug = slug.replace(' ', '')

    if truncate is not None:
        if not isinstance(truncate, int) or truncate <= 0:
            return None
        words = slug.split(separator)
        result = []
        current_length = 0
        for word in words:
            if not word:
                continue
            if current_length + len(word) + (1 if result else 0) <= truncate:
                if result:
                    result.append(separator)
                result.append(word)
                current_length += len(word) + (1 if result else 0)
            else:
                break
        slug = ''.join(result)

    if not slug:
        return None

    return slug