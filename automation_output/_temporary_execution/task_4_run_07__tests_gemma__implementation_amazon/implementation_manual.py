def get_read_duration(text):
    if not text:
        return 1
    words = text.split()
    word_count = len(words)
    read_speed = 200
    estimated_time = (word_count + 199) // 200
    return estimated_time
