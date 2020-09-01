from functools import wraps
import time


def logging_time(original_fn):
    @wraps(original_fn)
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print(
            "실행시간[{}]: {} Sec".format(
                original_fn.__name__, round(end_time - start_time, 2)
            )
        )
        return result

    return wrapper_fn
