import functools
import threading
import time


def ttl_cache(ttl_seconds, maxsize=None):
    def decorator(func):
        cache = {}
        lock = threading.Lock()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.monotonic()
            with lock:
                entry = cache.get(key)
                if entry is not None:
                    expires_at, value = entry
                    if now < expires_at:
                        return value
                    del cache[key]

            value = func(*args, **kwargs)

            with lock:
                if maxsize is not None and len(cache) >= maxsize:
                    for k in [k for k, (exp, _) in cache.items() if exp <= now]:
                        del cache[k]
                    if len(cache) >= maxsize:
                        oldest = min(cache, key=lambda k: cache[k][0])
                        del cache[oldest]
                cache[key] = (now + ttl_seconds, value)

            return value

        return wrapper

    return decorator
