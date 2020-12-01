import random
import string
import time
import textwrap
import numpy as np


def edit_distance(string_x, string_y):
    start_time = time.time()
    len_x, len_y = len(string_x), len(string_y)
    dp = [[0] * (len_x + 1) for i in range(len_y + 1)]
    for i in range(0, len_y + 1):
        dp[i][0] = i
    for j in range(0, len_x + 1):
        dp[0][j] = j
    for i in range(1, len_y + 1):
        for j in range(1, len_x + 1):
            if string_x[j - 1] == string_y[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
    end_time = time.time() - start_time
    # print(textwrap.fill("Edit Distance('{}', '{}') = {}".format(string_x, string_y, dp[len_y][len_x]), 100))
    # print(
    #     "----------------------------------------------------------------------------------------------------")
    return dp[len_y][len_x], end_time


if __name__ == "__main__":
    # template = "{0:<20}|{1:<20}|{2:<25}"  # column widths: 8, 10, 15, 7, 10
    # print(template.format("STRING LENGTH (N)", "EDIT DISTANCE", "TIME TAKEN (in s)"))
    all_times = [[0] * 10 for i in range(1000)]

    for x in range(1000):
        for n in range(100, 1001, 100):
            str1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
            str2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
            edit_dist, time_taken = edit_distance(str1, str2)
            all_times[x][(n // 100 - 1)] = time_taken
            # print(template.format(n, edit_dist, time_taken))
    a = np.array(all_times)
    print(a.shape)
    print(a.mean(axis=0))
    # string_1 = "BABBLE"
    # string_2 = "APPLE"
    # edit_dist, time_taken = edit_distance(string_1, string_2)
    #
    # string_1 = "ATCAT"
    # string_2 = "ATTATC"
    # edit_dist, time_taken = edit_distance(string_1, string_2)
    # assert edit_dist == 2
    #
    # string_1 = "taacttctagtacatacccgggttgagcccccatttcttggttggatgcgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat"
    # string_2 = "taacttctagtacatacccgggttgagcccccatttccgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat"
    # edit_dist, time_taken = edit_distance(string_1, string_2)
    # assert edit_dist == 11
    #
    # string_1 = "CGCAATTCTGAAGCGCTGGGGAAGACGGGT"
    # string_2 = "TATCCCATCGAACGCCTATTCTAGGAT"
    # edit_dist, time_taken = edit_distance(string_1, string_2)
    # assert edit_dist == 18
    #
    # string_1 = "tatttacccaccacttctcccgttctcgaatcaggaatagactactgcaatcgacgtagggataggaaactccccgagtttccacagaccgcgcgcgatattgctcgccggcatacagcccttgcgggaaatcggcaaccagttgagtagttcattggcttaagacgctttaagtacttaggatggtcgcgtcgtgccaa"
    # string_2 = "atggtctccccgcaagataccctaattccttcactctctcacctagagcaccttaacgtgaaagatggctttaggatggcatagctatgccgtggtgctatgagatcaaacaccgctttctttttagaacgggtcctaatacgacgtgccgtgcacagcattgtaataacactggacgacgcgggctcggttagtaagtt"
    # edit_dist, time_taken = edit_distance(string_1, string_2)
    # assert edit_dist == 112
