from datetime import datetime

def str_to_date(date_str):
    return datetime.strptime(date_str, '%m/%d/%Y').date()
