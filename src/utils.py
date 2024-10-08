import time

def retry_on_failure(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    time.sleep(delay)
        return wrapper
    return decorator

# Example usage:
# @retry_on_failure(max_attempts=5, delay=2)
# def some_function_that_might_fail():
#     # Your code here
#     pass