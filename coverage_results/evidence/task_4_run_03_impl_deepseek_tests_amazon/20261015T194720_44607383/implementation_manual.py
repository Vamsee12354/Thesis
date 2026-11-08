import math

def get_read_duration(text):
    if not text or text.isspace():
        return 1
    words = text.split()
    word_count = len(words)
    read_time = math.ceil(word_count / 200)
    return max(read_time, 1)