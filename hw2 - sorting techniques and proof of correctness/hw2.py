import random
from time import time


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
    for x in range(100, 10100, 100):
        nums = random.sample(range(1, 10100), x)
        nums_copy = nums[:]
        # print("before merge sort:", nums_copy)

        # merge_sort_recursive(nums, 0, len(nums) - 1)
        start_time = time()
        merge_sort_recursive(nums, 0, len(nums) - 1)
        time_taken = time() - start_time
        merge_time.append(time_taken * 1000)
        # print("after merge sort:", nums)

        # print("before quick sort:", nums_copy)
        # quick_sort_recursive(nums_copy, 0, len(nums_copy) - 1)
        start_time = time()
        quick_sort_recursive(nums_copy, 0, len(nums_copy) - 1)
        time_taken = time() - start_time
        quick_time.append(time_taken * 1000)
        # print("after quick sort:", nums_copy)

    for y in range(len(merge_time)):
        print(merge_time[y], quick_time[y])
