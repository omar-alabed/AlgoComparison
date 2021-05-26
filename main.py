import random
import sys
import time

from sorting_algorithms.bitonic_merge_sort import bitonicSort
from sorting_algorithms.parallel_merge_sort import parallel_sort, merge_sort
# from sorting_algorithms.serial_merge_sort import merge_sort

if __name__ == "__main__":
    size = int(sys.argv[-1]) if sys.argv[-1].isdigit() else False

    if not size:
        size = 1024
        for i in range(100):
            print('SIZE\t\t' ,'USED ALGORITHM\t\t', 'IS THE RESULT SORTED?\t\t', 'TIME')
            data_unsorted = [random.randint(0, size) for _ in range(size)]
            for sort in merge_sort, parallel_sort:
                start = time.time()
                data_sorted = sort(data_unsorted)
                end = time.time() - start
                print (f'{size}\t\t', f'{sort.__name__}\t\t', sorted(data_unsorted) == data_sorted, '\t\t', end)

            start = time.time()
            data_sorted = bitonicSort(True, data_unsorted)
            end = time.time() - start
            print(f'{size}\t\t', 'bitonic_sort\t\t',sorted(data_unsorted) == data_sorted, '\t\t', end, '\n')

            size = size * 2
    else:
        print('SIZE\t\t' ,'USED ALGORITHM\t\t', 'IS THE RESULT SORTED?\t\t', 'TIME')
        data_unsorted = [random.randint(0, size) for _ in range(size)]
        for sort in merge_sort, parallel_sort:
            start = time.time()
            data_sorted = sort(data_unsorted)
            end = time.time() - start
            print (f'{size}\t\t', f'{sort.__name__}\t\t', sorted(data_unsorted) == data_sorted, '\t\t', end,)

        start = time.time()
        data_sorted = bitonicSort(True, data_unsorted)
        end = time.time() - start
        print(f'{size}\t\t', 'bitonic_sort\t\t', sorted(data_unsorted) == data_sorted, '\t\t', end, '\n')