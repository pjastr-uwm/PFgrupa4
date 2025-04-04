from datetime import datetime


def generate_unique_filename():
    now = datetime.now()
    return f"file_{now.strftime("%Y%m%d_%H%M%S")}.txt"