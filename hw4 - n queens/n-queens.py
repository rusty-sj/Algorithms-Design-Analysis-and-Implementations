import time


def b_queens(row, n, placement, solutions):  # backtrack search
    if row == n:  # when row reaches n, we have placed all the n queens without any attack conflicts
        if is_valid(placement):
            solutions.append(placement)
            placement = []
    else:
        for column in range(n):  # explore n columns for row'th queen
            placement.append(column)
            print(placement)
            b_queens(row + 1, n, placement, solutions)


def is_valid(placement):
    row_id = len(placement) - 1
    # 0 to row_id - 1 queens are placed without attack conflicts
    for i in range(row_id):  # compare newly placed row_id'th queen with already placed queens for attacks
        diff = abs(placement[i] - placement[row_id])
        if diff == 0 or diff == row_id - i:  # same column clash or diagonal clash
            return False
    return True


if __name__ == '__main__':
    N = 4
    for i in range(1, N + 1):
        solutions_b_queens = []
        start_b = time.time()
        b_queens(0, i, [], solutions_b_queens)
        b_time = (time.time() - start_b)
        print("{}\t {}\t {}".format(i, len(solutions_b_queens), b_time))
