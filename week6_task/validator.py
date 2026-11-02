import re

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
time_pattern = r'^([01]\d|2[0-3]):([0-5]\d)$'

def validate_email(email):
    if re.match(email_pattern,email):
        return True
    return False

def validate_time(login_time):
    if re.match(time_pattern,login_time):
        return True
    return False

def validate_record(line):
    parts = line.strip().split()
    if len(parts)!=3:
        return False
    username,email,login_time = parts
    if validate_email(email) and validate_time(login_time):
        return True
    return False