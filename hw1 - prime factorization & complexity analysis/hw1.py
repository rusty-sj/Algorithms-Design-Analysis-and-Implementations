from time import time


def factors(number):
    start_time = time()
    output = []  # output array to store factors

    if number == 1:
        return output  # 1 is not a prime

    # Reduce the number until it can be divided by 2
    while number % 2 == 0:  # worst case runs log_2(N) times,  O (log_2 N)
        output.append(2)
        number = number // 2

    # For each number from 3 to sqrt n, keep dividing number whenever possible and add to factors
    # since even numbers are already taken care of by previous loop, increment by 2
    for i in range(3, int(number ** (1 / 2)) + 1):  # worst case runs sqrt N times, O (sqrt N)
        while number % i == 0:  # worst case runs log_3 N times, otherwise log_i N
            output.append(i)
            number = number // i
        i += 2

    if number > 2:  # number hasn't been divided by anything, it's prime
        output.append(number)

    time_taken = time() - start_time
    times.append(time_taken)
    return output


def verify(number, factors_list):
    product = 1
    for factor in factors_list:
        product *= factor
    return number == product


if __name__ == '__main__':
    times = []
    numbers = [6, 60, 840, 7560, 83160, 720720, 8648640, 73513440, 735134400, 6983776800, 97772875200, 963761198400,
               9316358251200, 97821761637600, 866421317361600, 8086598962041600, 74801040398884800, 897612484786617600]
    # numbers = [170141183460469231731687303715884105727]
    for num in numbers:
        factors_list = factors(number=num)
        # print(verify(number=num, factors_list=factors_list))

    for i in range(0, len(numbers)):
        print('{} \t {}'.format(numbers[i], times[i] * 1000))

    # factors_list = factors(number=1)
    # print(verify(number=1, factors_list=factors_list))
