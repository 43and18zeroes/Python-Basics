import concurrent.futures
import time

def sleep_and_return(sec):
    time.sleep(sec)
    return sec

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(sleep_and_return, i) for i in range(5)]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
