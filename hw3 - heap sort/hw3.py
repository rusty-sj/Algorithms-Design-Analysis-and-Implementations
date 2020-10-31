import random
from time import time


# Time Complexity: O(n log n) + O(n)
# Space Complexity: O(log n) for recursive stack space of max_heapify
def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr, n)  # O(n)
    for i in range(n - 1, 0, -1):  # delete n elements one by one from top, heapify
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


# assumes part of heap is sorted: log(n)
def max_heapify(arr, n, i):  # log n
    maximum = i
    left = (2 * i) + 1
    right = (2 * i) + 2
    if left < n and arr[i] < arr[left]:
        maximum = left
    if right < n and arr[maximum] < arr[right]:
        maximum = right
    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]
        max_heapify(arr, n, maximum)


# build max heap from unsorted array: O(n)
def build_max_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


# Time Complexity: O(n log n)
# Space Complexity: O(log n) stack space for recursion + O(n) array after merge
def merge_sort_recursive(numbers, low, high):
    if low < high:
        middle = (low + high) // 2
        merge_sort_recursive(numbers, low, middle)
        merge_sort_recursive(numbers, middle + 1, high)
        merge(numbers, low, middle, high)


def merge(numbers, low, mid, high):
    i = low
    j = mid + 1
    sorted_nums = []
    while i <= mid and j <= high:
        if numbers[i] < numbers[j]:
            sorted_nums.append(numbers[i])
            i += 1
        else:
            sorted_nums.append(numbers[j])
            j += 1

    while i <= mid:
        sorted_nums.append(numbers[i])
        i += 1
    while j <= high:
        sorted_nums.append(numbers[j])
        j += 1
    numbers[low:high + 1] = sorted_nums[:]


# Time Complexity: O(n log n); worst case O(n^2) when list is already sorted
# Space Complexity: O(log n) stack space for recursion; O(n) stack in worst case
def quick_sort_recursive(numbers, low, high):
    if low >= high:
        return
    partition_index = partition(numbers, low, high)
    quick_sort_recursive(numbers, low, partition_index - 1)
    quick_sort_recursive(numbers, partition_index, high)


def partition(numbers, low, high):
    pivot = numbers[(low + high) // 2]  # Take middle element as pivot
    while low <= high:
        while numbers[low] < pivot:
            low += 1
        while numbers[high] > pivot:
            high -= 1
        if low <= high:
            numbers[low], numbers[high] = numbers[high], numbers[low]
            # swap(numbers, low, high)
            low += 1
            high -= 1
    return low  # new partition position, every left is smaller than pivot, every right is bigger than pivot


if __name__ == '__main__':
    merge_time = []
    quick_time = []
    heap_time = []
    xs = []
    for x in range(100, 10100, 100):
        xs.append(x)
        # nums_merge = list(range(1, x + 1))
        nums_merge = random.sample(range(1, 10100), x)
        # print(nums_merge)
        nums_quick = nums_merge[:]
        nums_heap = nums_merge[:]

        start_time = time()
        merge_sort_recursive(nums_merge, 0, len(nums_merge) - 1)
        time_taken = time() - start_time
        merge_time.append(time_taken * 1000)

        start_time = time()
        quick_sort_recursive(nums_quick, 0, len(nums_quick) - 1)
        time_taken = time() - start_time
        quick_time.append(time_taken * 1000)

        start_time = time()
        heap_sort(nums_heap)
        time_taken = time() - start_time
        heap_time.append(time_taken * 1000)

    for y in range(len(merge_time)):
        print(xs[y], merge_time[y], quick_time[y], heap_time[y])
