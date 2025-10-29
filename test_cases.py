from utils import generate_array, check_sorted, check_max
from threaded_sort import threaded_sort
from process_sort import process_sort
from threaded_max import threaded_max
from process_max import process_max

def run_tests():
    sizes = [32, 131072]
    workers = [1, 2, 4, 8]
    for size in sizes:
        arr = generate_array(size)
        print(f"\nTesting size={size}")
        for n in workers:
            assert check_sorted(threaded_sort(arr, n)), "Threaded sort failed"
            assert check_sorted(process_sort(arr, n)), "Process sort failed"
            assert check_max(arr, threaded_max(arr, n)), "Threaded max failed"
            assert check_max(arr, process_max(arr, n)), "Process max failed"
            print(f"  workers={n}: All tests passed")

if __name__ == "__main__":
    run_tests()
