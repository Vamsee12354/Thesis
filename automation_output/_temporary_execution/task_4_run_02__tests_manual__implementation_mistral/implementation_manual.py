def get_read_duration(text):
    if not isinstance(text, str):
        return None

    words = text.split()
    word_count = len(words)

    if word_count == 0:
        return 1

    read_time = word_count / 200
    return max(1, int(read_time) + (1 if read_time % 1 > 0 else 0))