import math
def get_read_duration(text):
    if len(text.split())>0:
        time=math.ceil(len(text.split())/200)
    else:
        time=1
    return time
text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat."
print(get_read_duration(text))