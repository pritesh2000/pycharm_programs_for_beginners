import time
from functools import lru_cache


@lru_cache(maxsize=3)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work...")
    some_work(3)
    some_work(1)        # here it takes 3 value as cache because maxsize is 3
    some_work(4)
    some_work(5)
    print("Done... Calling again")
    some_work(3)        # So these three take 3 seconds to run
    print("Called again")
