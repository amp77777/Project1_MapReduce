from multiprocessing import Process, Value, Lock
from utils import chunk_array, generate_array, check_max, measure_time_and_memory

def find_local_max(chunk, shared_max, lock):
    local_max = max(chunk)
    with lock:
        if local_max > shared_max.value:
            shared_max.value = local_max

def process_max(arr, n_workers):
    shared_max = Value('i', float('-inf'))
    lock = Lock()
    chunks = chunk_array(arr, n_workers)
    processes = []
    for chunk in chunks:
        p = Process(target=find_local_max, args=(chunk, shared_max, lock))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    return shared_max.value

if __name__ == "__main__":
    for size in [32, 131072]:
        arr = generate_array(size)
        for n_workers in [1, 2, 4, 8]:
            computed_max, exec_time, mem_diff = measure_time_and_memory(process_max, arr, n_workers)
            print(f"[Process Max] size={size} workers={n_workers} time={exec_time:.4f}s mem_change={mem_diff:.2f}MB correct={check_max(arr, computed_max)}")
