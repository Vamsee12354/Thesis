def get_read_duration(text):
    try:
        words = text.split()
        word_count = len(words)
        read_time = (word_count + 199) // 200
        return max(read_time, 1)
    except Exception:
        return None