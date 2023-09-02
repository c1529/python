from concurrent.futures import ThreadPoolExecutor
import test1

with ThreadPoolExecutor(max_workers=4) as k:
    for page in range(1, 100):
        try:
            k.submit(test1.main, page)
        except Exception as e:
            print(e)
