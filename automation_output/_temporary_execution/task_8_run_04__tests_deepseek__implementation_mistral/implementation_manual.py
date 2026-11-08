def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text:
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

    translit_map = {
        ' ': separator,
        '，': separator,
        '。': separator,
        '！': separator,
        '？': separator,
        '、': separator,
        '；': separator,
        '：': separator,
        '（': separator,
        '）': separator,
        '【': separator,
        '】': separator,
        '「': separator,
        '」': separator,
        '『': separator,
        '』': separator,
        '“': separator,
        '”': separator,
        '‘': separator,
        '’': separator,
        '—': separator,
        '…': separator,
        '～': separator,
        '·': separator,
        '、': separator,
        '。': separator,
        '，': separator,
        '；': separator,
        '：': separator,
        '（': separator,
        '）': separator,
        '【': separator,
        '】': separator,
        '「': separator,
        '」': separator,
        '『': separator,
        '』': separator,
        '“': separator,
        '”': separator,
        '‘': separator,
        '’': separator,
    }

    try:
        normalized = text.strip()
        if not normalized:
            return None

        slug_parts = []
        current_part = []

        for char in normalized:
            if char in ignore:
                if current_part:
                    slug_parts.append(''.join(current_part))
                    current_part = []
                slug_parts.append(char)
            else:
                lower_char = char.lower()
                if lower_char in translit_map:
                    replacement = translit_map[lower_char]
                    if replacement == separator:
                        if current_part:
                            slug_parts.append(''.join(current_part))
                            current_part = []
                    else:
                        current_part.append(replacement)
                else:
                    if char.isalnum():
                        current_part.append(char)
                    else:
                        if current_part:
                            slug_parts.append(''.join(current_part))
                            current_part = []

        if current_part:
            slug_parts.append(''.join(current_part))

        if not slug_parts:
            return None

        slug = separator.join(slug_parts)

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