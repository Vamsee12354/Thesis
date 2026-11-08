def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if not text:
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    if not isinstance(separator, str) or len(separator) != 1:
        return None

    if not isinstance(lowercase, bool):
        return None

    if truncate is not None and (not isinstance(truncate, int) or truncate <= 0):
        return None

    try:
        normalized = text.encode('utf-8', 'ignore').decode('utf-8')
    except Exception:
        return None

    if not normalized:
        return None

    slug_parts = []
    current_part = []
    in_word = False

    for char in normalized:
        if char in ignore:
            if current_part:
                slug_parts.append(''.join(current_part))
                current_part = []
            slug_parts.append(char)
            in_word = False
            continue

        if char.isalnum():
            current_part.append(char)
            in_word = True
        else:
            if in_word:
                slug_parts.append(''.join(current_part))
                current_part = []
                in_word = False

    if current_part:
        slug_parts.append(''.join(current_part))

    if not slug_parts:
        return None

    if lowercase:
        processed_parts = [part.lower() for part in slug_parts]
    else:
        processed_parts = slug_parts

    if separator:
        slug = separator.join(processed_parts)
    else:
        slug = ''.join(processed_parts)

    if truncate is not None and len(slug) > truncate:
        if separator:
            words = slug.split(separator)
            truncated_parts = []
            current_length = 0
            for word in words:
                if current_length + len(word) + (1 if truncated_parts else 0) <= truncate:
                    if truncated_parts:
                        truncated_parts.append(separator)
                    truncated_parts.append(word)
                    current_length += len(word) + (1 if truncated_parts else 0)
                else:
                    break
            slug = ''.join(truncated_parts)
        else:
            slug = slug[:truncate]

    if not slug:
        return None

    return slug