import file_handler
import processor

def main():
    lines = file_handler.read_log_file("log.txt")

    if len(lines)==0:
        print("No records to process")
        return

    valid_records,invalid_lines,upper_usernames = processor.process_records(lines)

    print("\n----- Valid Records -----")
    i=0
    for record in valid_records:
        username,email,login_time = record
        print(upper_usernames[i],"|",email,"|",login_time)
        i=i+1

    file_handler.write_invalid_records("invalid_log.txt",invalid_lines)
    print("\nInvalid records have been written to invalid_log.txt")

    file_handler.save_pickle("valid_records.pkl",valid_records)
    print("Valid records saved to valid_records.pkl")

    loaded_data = file_handler.load_pickle("valid_records.pkl")
    print("\n----- Data Loaded Back From Pickle File -----")
    for record in loaded_data:
        print(record)

if __name__=="__main__":
    try:
        main()
    except Exception as e:
        print("Program stopped because of an error:",e)