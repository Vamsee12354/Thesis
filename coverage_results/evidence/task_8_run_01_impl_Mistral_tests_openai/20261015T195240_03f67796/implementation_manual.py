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

        slug_parts = []
        current_part = []
        in_word = False

        for char in normalized:
            if char in ignore:
                if current_part:
                    slug_parts.append("".join(current_part))
                    current_part = []
                slug_parts.append(char)
                in_word = False
            elif char.isalnum():
                current_part.append(char)
                in_word = True
            else:
                if in_word:
                    slug_parts.append("".join(current_part))
                    current_part = []
                    in_word = False

        if current_part:
            slug_parts.append("".join(current_part))

        if not slug_parts:
            return None

        processed_parts = []
        for part in slug_parts:
            if part in ignore:
                processed_parts.append(part)
            else:
                transliterated = []
                for c in part:
                    if c.isascii() and c.isalnum():
                        transliterated.append(c)
                    else:
                        try:
                            import unicodedata
                            norm = unicodedata.normalize('NFKD', c)
                            for n in norm:
                                if n.isalnum():
                                    transliterated.append(n.lower() if lowercase else n)
                                    break
                        except:
                            pass
                if transliterated:
                    processed_parts.append("".join(transliterated))

        if not processed_parts:
            return None

        slug = separator.join(processed_parts)

        if lowercase:
            slug = slug.lower()

        if truncate is not None and len(slug) > truncate:
            last_sep_index = slug.rfind(separator)
            if last_sep_index == -1:
                slug = slug[:truncate]
            else:
                slug = slug[:last_sep_index]

        if not slug:
            return None

        return slug

    except Exception:
        return None