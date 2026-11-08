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
        normalized = text.strip()
        if not normalized:
            return None

        if ignore:
            for char in ignore:
                normalized = normalized.replace(char, '')

        slug = []
        i = 0
        n = len(normalized)

        while i < n:
            char = normalized[i]
            if char.isspace():
                if slug and slug[-1] != separator:
                    slug.append(separator)
                i += 1
            elif char.isalnum():
                slug.append(char)
                i += 1
            else:
                i += 1

        if not slug:
            return None

        if separator in slug:
            slug = [s for s in slug if s != separator]
            if not slug:
                return None

        if lowercase:
            slug = [c.lower() for c in slug]

        result = ''.join(slug)

        if truncate is not None and len(result) > truncate:
            if separator in result:
                parts = result.split(separator)
                truncated_parts = []
                current_length = 0
                for part in parts:
                    if current_length + len(part) + (1 if truncated_parts else 0) <= truncate:
                        truncated_parts.append(part)
                        current_length += len(part) + (1 if truncated_parts else 0)
                    else:
                        break
                result = separator.join(truncated_parts)
            else:
                result = result[:truncate]

        if not result:
            return None

        return result

    except Exception:
        return None