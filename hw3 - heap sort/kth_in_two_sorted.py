def find_kth(list1, list2, start1, end1, start2, end2, k):
    # Edge case 1: k greater than size of list1 + list2
    if k > len(list1) + len(list2):
        print("Invalid k: not in range of combined lists")
        return -1

    # Edge case 2: If list1 is exhausted, kth element is the kth in list2
    if start1 > end1:
        return list2[start2 + k - 1]

    # Edge case 3: If list2 is exhausted, kth element is the kth in list1
    if start2 > end2:
        return list1[start1 + k - 1]

    # Core Logic: calculate mid elements of list1 and list2
    mid1 = (start1 + end1) // 2
    mid2 = (start2 + end2) // 2

    # if k is less than number of elements in list1[start1...mid1] and list2[start2...mid2] combined,
    # the kth element lies in range and so we halve search space by manipulating mids, moving to right halves
    if (mid1 - start1 + 1 + mid2 - start2 + 1) > k:
        if list1[mid1] > list2[mid2]:  # get rid of right half of list1
            print("computation")
            return find_kth(list1, list2, start1, mid1 - 1, start2, end2, k)
        else:  # get rid of right half of list2
            print("computation")
            return find_kth(list1, list2, start1, end1, start2, mid2 - 1, k)

    # k is not within the range of combined list1[start1...mid1] and list2[start2...mid2],
    # we shift the search space by halving lists and manipulating k
    else:
        if list1[mid1] > list2[mid2]:  # move to right half of list2, change k by factor of shift
            print("computation")
            return find_kth(list1, list2, start1, end1, mid2 + 1, end2, k - (mid2 - start2 + 1))
        else:  # move to right half of list1, change k by factor of shift
            print("computation")
            return find_kth(list1, list2, mid1 + 1, end1, start2, end2, k - (mid1 - start1 + 1))


if __name__ == '__main__':
    array1 = [1, 3, 5, 7, 9, 11, 12]
    array2 = [4, 5, 6]

    # array1 = [10, 30, 40, 50]
    # array2 = [30, 50, 100, 110]
    print(find_kth(array1, array2, 0, 0, len(array1) - 1, len(array2) - 1, 2))
