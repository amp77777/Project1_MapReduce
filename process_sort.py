from multiprocessing import Process, Queue
from utils import chunk_array, generate_array, check_sorted, measure_time_and_memory

def sort_chunk(chunk, out_q):
    sorted_chunk = sorted(chunk)
    out_q.put(sorted_chunk)

def merge_sorted_chunks(chunks):
    import heapq
    return list(heapq.merge(*chunks))

def process_sort(arr, n_workers):
    chunks = chunk_array(arr, n_workers)
    out_q = Queue()
    processes = []
    for chunk in chunks:
        p = Process(target=sort_chunk, args=(chunk, out_q))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

    sorted_chunks = []
    while not out_q.empty():
        sorted_chunks.append(out_q.get())
    sorted_arr = merge_sorted_chunks(sorted_chunks)
    return sorted_arr

if __name__ == "__main__":
    for size in [32, 131072]:
        arr = generate_array(size)
        for n_workers in [1, 2, 4, 8]:
            sorted_arr, exec_time, mem_diff = measure_time_and_memory(process_sort, arr, n_workers)
            print(f"[Process Sort] size={size} workers={n_workers} time={exec_time:.4f}s mem_change={mem_diff:.2f}MB correct={check_sorted(sorted_arr)}")
