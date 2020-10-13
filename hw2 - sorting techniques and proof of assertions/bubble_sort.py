def bubble_sort(a):
    swap, j = 1, len(a)
    # Assertion 0: a[0], ..., a[n - 1] is an array of integers with at least 1 element
    while swap == 1:
        # Assertion 1: swap = 1 && a'[j] <= ... <= a'[n - 1] && {a’[j], ...,a’[n - 1]} = {a[j], ..., a[n - 1]}
        swap = 0
        j = j - 1
        for i in range(j):
            # Assertion 2: a[i] is pointing to max a[0]...a[i]
            print(i, j)
            print(a)
            if a[i] > a[i + 1]:
                a[i], a[i + 1], swap = a[i + 1], a[i], 1
    # Assertion 3: a’[0] <= ...<= a’[n - 1] & {a’[0], ..., a’[n - 1]} = {a[0], ..., a[n - 1]}


if __name__ == '__main__':
    input = [3, 5, 2, 9, 1]
    # input = [9, 6, 3, 1, 0]
    # input = [1, 2, 3, 4, 5]
    # input = [5, 4, 3, 2, 1]
    bubble_sort(input)
    print(input)
