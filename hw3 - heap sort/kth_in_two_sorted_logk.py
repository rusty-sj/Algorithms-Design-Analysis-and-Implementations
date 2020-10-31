def find_kth(list1, list2, k):
    if k > len(list1) + len(list2):
        print("k greater than combined list's length")
        return -1
    if not list1:
        return list2[k - 1]
    elif not list2:
        return list1[k - 1]
    elif k == 1:
        return min(list1[0], list2[0])

    mid1 = min(len(list1), k // 2)
    mid2 = min(len(list2), k // 2)
    print(mid1, mid2)
    if list1[mid1 - 1] < list2[mid2 - 1]:
        return find_kth(list1[mid1:], list2, k - mid1)
    return find_kth(list1, list2[mid2:], k - mid2)


if __name__ == '__main__':
    array1 = [1, 3, 5, 7, 9, 11, 12]
    array2 = [4, 5, 6]

    # array1 = [10, 30, 40, 50]
    # array2 = [30, 50, 100, 110]
    print(kth_element(array1, array2, 0, 0, len(array1) - 1, len(array2) - 1, 2))
