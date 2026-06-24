import math

def get_read_duration(text):
    if not text or text.isspace():
        return 1
    word_count = len(text.split())
    minutes = math.ceil(word_count / 200)
    return max(minutes, 1)