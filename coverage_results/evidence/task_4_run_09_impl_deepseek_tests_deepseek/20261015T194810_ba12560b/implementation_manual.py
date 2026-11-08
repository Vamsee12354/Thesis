def get_read_duration(text):
    if not isinstance(text, str):
        return 1
    words = text.split()
    word_count = len(words)
    minutes = max(1, (word_count + 199) // 200)
    return minutes
