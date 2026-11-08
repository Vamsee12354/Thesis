def get_read_duration(text):
    if not text or not text.strip():
        return 1

    words = text.split()
    word_count = len(words)

    if word_count == 0:
        return 1

    read_time = word_count / 200
    return max(1, int(read_time) if read_time.is_integer() else int(read_time) + 1)