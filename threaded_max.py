import threading
from utils import chunk_array, generate_array, check_max, measure_time_and_memory

class SharedMax:
    def __init__(self):
        self.value = float('-inf')
        self.lock = threading.Lock()

def find_local_max(chunk, shared_max):
    local_max = max(chunk)
    with shared_max.lock:
        if local_max > shared_max.value:
            shared_max.value = local_max

def threaded_max(arr, n_workers):
    shared_max = SharedMax()
    chunks = chunk_array(arr, n_workers)
    threads = []
    for chunk in chunks:
        t = threading.Thread(target=find_local_max, args=(chunk, shared_max))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return shared_max.value

if __name__ == "__main__":
    for size in [32, 131072]:
        arr = generate_array(size)
        for n_workers in [1, 2, 4, 8]:
            computed_max, exec_time, mem_diff = measure_time_and_memory(threaded_max, arr, n_workers)
            print(f"[Threaded Max] size={size} workers={n_workers} time={exec_time:.4f}s mem_change={mem_diff:.2f}MB correct={check_max(arr, computed_max)}")
