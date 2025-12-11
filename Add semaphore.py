import threading
import time

sem = threading.Semaphore(2)

def worker(id):
    with sem:
        print(f"Worker {id} starting")
        time.sleep(1)
        print(f"Worker {id} done")

for i in range(5):
    threading.Thread(target=worker, args=(i,)).start()
