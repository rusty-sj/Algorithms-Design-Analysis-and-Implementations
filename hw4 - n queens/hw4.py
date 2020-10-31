import time
from itertools import permutations


def e_queens(n, solutions):  # exhaustive search
    # Generate all possible permutations representing Q1->index 0, Q2->index1, ..., Qn->index n - 1
    for perm in permutations(range(n)):
        if is_valid_perm(perm, n):  # Check if attack conditions are met
            solutions.append(perm)


def is_valid_perm(permutation, n):
    for row_id in range(n):  # for each queen
        for i in range(row_id):  # compare queen at row_id's placement with the other columns
            if abs(permutation[i] - permutation[row_id]) == row_id - i:  # diagonal clash check
                return False
    return True


def b_queens(row, n, placement, solutions):  # backtrack search
    if row == n:  # when row reaches n, we have placed all the n queens without any attack conflicts
        solutions.append(placement[:])
    else:
        for column in range(n):  # explore n columns for row'th queen
            placement.append(column)
            # print(placement)
            if is_valid(placement):  # check if the row'th queen placed at column attacks already placed queens
                b_queens(row + 1, n, placement, solutions)
            placement.pop()  # done exploring column'th position


def is_valid(placement):
    row_id = len(placement) - 1
    # 0 to row_id - 1 queens are placed without attack conflicts
    for i in range(row_id):  # compare newly placed row_id'th queen with already placed queens for attacks
        diff = abs(placement[i] - placement[row_id])
        if diff == 0 or diff == row_id - i:  # same column clash or diagonal clash
            return False
    return True


if __name__ == '__main__':
    N = 8
    for i in range(1, N + 1):
        solutions_e_queens = []
        start_e = time.time()
        e_queens(i, solutions_e_queens)
        e_time = (time.time() - start_e)

        solutions_b_queens = []
        start_b = time.time()
        b_queens(0, i, [], solutions_b_queens)
        b_time = (time.time() - start_b)
        print("{}\t {}\t {}\t {}\t {}".format(i, len(solutions_e_queens), len(solutions_b_queens), e_time, b_time))
