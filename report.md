# Project Report: MapReduce Parallel Sorting & Max-Value Aggregation

## 1. Project Description

This project implements two MapReduce-style tasks on a single machine:
- **Parallel Sorting**: Splitting an array, sorting chunks in parallel, and merging.
- **Max-Value Aggregation**: Finding global max using a shared memory buffer with synchronization.

## 2. Instructions

See README.md for step-by-step instructions.

## 3. Structure & Diagrams

- Thread/process workers created for map phase.
- IPC via Queue (process/thread) for sorted chunks.
- Shared memory & lock for max-value aggregation.

```
[Main Controller]
      |--[Worker 1]--|
      |--[Worker 2]--|----> [Reducer] (merges/aggregates)
      ...
```

## 4. Implementation

- **Tools:** Python, threading, multiprocessing, psutil.
- **Process Management:** Manual creation/joining of threads/processes.
- **IPC:** Queue (for sorting), shared memory Value + Lock (for max).
- **Synchronization:** threading.Lock, multiprocessing.Lock.
- **Performance:** Time and memory usage via utils.py.

## 5. Performance Evaluation

- Correctness for size=32: Verified.
- Timing/memory for size=131072: See terminal outputs.
- Threading vs Processing: Processing generally uses more memory, threading can be faster for CPU-bound tasks if GIL isn't limiting.

## 6. Conclusion

- Both models work correctly.
- Synchronization overhead is visible, especially with more workers.
- Possible improvements: Use thread/process pools, optimize chunk merge.
