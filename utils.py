import time
import random
import psutil
import os

def chunk_array(arr, n_chunks):
    chunk_size = len(arr) // n_chunks
    chunks = [arr[i*chunk_size:(i+1)*chunk_size] for i in range(n_chunks)]
    if len(arr) % n_chunks:
        chunks[-1].extend(arr[n_chunks*chunk_size:])
    return chunks

def generate_array(size, seed=42):
    random.seed(seed)
    return [random.randint(0, size * 10) for _ in range(size)]

def check_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def check_max(arr, computed_max):
    return computed_max == max(arr)

def measure_time_and_memory(func, *args, **kwargs):
    start_time = time.time()
    process = psutil.Process(os.getpid())
    start_mem = process.memory_info().rss
    result = func(*args, **kwargs)
    end_time = time.time()
    end_mem = process.memory_info().rss
    return result, end_time - start_time, (end_mem - start_mem)/1024/1024  # MB
