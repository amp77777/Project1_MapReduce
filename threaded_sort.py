import threading
from queue import Queue
from utils import chunk_array, generate_array, check_sorted, measure_time_and_memory

def sort_chunk(chunk, out_q):
    sorted_chunk = sorted(chunk)
    out_q.put(sorted_chunk)

def merge_sorted_chunks(chunks):
    import heapq
    return list(heapq.merge(*chunks))

def threaded_sort(arr, n_workers):
    chunks = chunk_array(arr, n_workers)
    out_q = Queue()
    threads = []
    for chunk in chunks:
        t = threading.Thread(target=sort_chunk, args=(chunk, out_q))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    sorted_chunks = []
    while not out_q.empty():
        sorted_chunks.append(out_q.get())
    sorted_arr = merge_sorted_chunks(sorted_chunks)
    return sorted_arr

if __name__ == "__main__":
    for size in [32, 131072]:
        arr = generate_array(size)
        for n_workers in [1, 2, 4, 8]:
            sorted_arr, exec_time, mem_diff = measure_time_and_memory(threaded_sort, arr, n_workers)
            print(f"[Threaded Sort] size={size} workers={n_workers} time={exec_time:.4f}s mem_change={mem_diff:.2f}MB correct={check_sorted(sorted_arr)}")
