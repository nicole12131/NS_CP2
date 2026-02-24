# NS 1st word counter 

from datetime import datetime


def get_current_timestamp():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time