from validator import validate_record
from utils.decorators import log_execution

@log_execution
def process_records(lines):
    valid_lines = list(filter(lambda line:validate_record(line),lines))
    invalid_lines = list(filter(lambda line:not validate_record(line),lines))

    valid_records=[]
    for line in valid_lines:
        parts=line.strip().split()
        username,email,login_time=parts
        valid_records.append((username,email,login_time))

    upper_usernames=list(map(lambda rec:rec[0].upper(),valid_records))

    return valid_records,invalid_lines,upper_usernames