def get_read_duration(text):
    if len(text.split())>0:
        time=len(text.split())/200
    else:
        time=0
    return time
text=""
print(get_read_duration(text))