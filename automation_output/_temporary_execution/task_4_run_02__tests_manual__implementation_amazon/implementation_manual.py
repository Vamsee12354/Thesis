def get_read_duration(text):
    if not text:
        return 1
    
    words = text.split()
    word_count = len(words)
    
    if word_count == 0:
        return 1
    
    read_speed = 200
    read_time = (word_count + 199) // 200
    
    return read_time
