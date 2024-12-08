import time
from datetime import timedelta
from functools import wraps

def retry(count=3, delay = timedelta, handled_exceptions=()):
    if count < 1:
        raise ValueError("Параметр count должен быть не менее 1.")

    if not handled_exceptions:
        handled_exceptions = (Exception,)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(count):
                start_time = time.time()
                try:
                    return func(*args, **kwargs)
                except handled_exceptions as e:
                    last_exception = e
                    time.sleep(start_time + delay.total_seconds() - time.time())
            raise last_exception
        return wrapper
    return decorator