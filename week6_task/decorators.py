import time

def log_execution(func):
    def wrapper(*args,**kwargs):
        print("Function started")
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print("Function completed")
        print("Time taken:",round(end_time-start_time,5),"seconds")
        return result
    return wrapper