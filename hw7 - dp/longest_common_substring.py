def longest_common_substring(string1, string2):
    n = len(string1)
    m = len(string2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    len_longest, longest_row, longest_col = 0, -1, -1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > len_longest:
                    len_longest = dp[i][j]
                    longest_row = i
                    longest_col = j

    if len_longest == 0:
        return ''

    common_string = ''
    i = len_longest
    while i > 0:
        common_string += string1[longest_row - 1]
        longest_row -= 1
        longest_col -= 1
        i -= 1
    return len_longest, common_string[::-1]


if __name__ == '__main__':
    print(longest_common_substring("Philanthropic", "Misanthropist"))
