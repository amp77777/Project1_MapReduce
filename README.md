# MapReduce Systems for Parallel Sorting and Max-Value Aggregation
## Overview

This project demonstrates MapReduce-style parallelism using both multithreading and multiprocessing for two tasks:
- **Parallel Sorting** of large arrays
- **Max-Value Aggregation** with constrained shared memory

## Structure

- `threaded_sort.py` - Multithreaded parallel sorting
- `process_sort.py` - Multiprocessing parallel sorting
- `threaded_max.py` - Multithreaded max-value aggregation
- `process_max.py` - Multiprocessing max-value aggregation
- `utils.py` - Shared utilities
- `test_cases.py` - Correctness tests

## How to Run

1. Install dependencies (`psutil`)
   ```bash
   pip install psutil
   ```
2. Run sorting experiments:
   ```bash
   python threaded_sort.py
   python process_sort.py
   ```
3. Run max-value experiments:
   ```bash
   python threaded_max.py
   python process_max.py
   ```
4. Run all correctness tests:
   ```bash
   python test_cases.py
   ```

## Diagrams

![Architecture Diagram](diagrams/architecture.png)

See `report.md` for full documentation and discussion.
