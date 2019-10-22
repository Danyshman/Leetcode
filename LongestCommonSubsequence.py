def longestCommonSubsequence(text1, text2):
    arr = [[0 for __ in range(len(text2)+1)] for __ in range(len(text1)+1)]
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                arr[i+1][j+1] = arr[i][j] + 1
            else:
                arr[i+1][j+1] = max(arr[i][j+1], arr[i+1][j])
    return arr[-1][-1]


print(longestCommonSubsequence("lcnqdmvsdopkvqvejijcdyxetuzonuhuzkpelmva","bklgfivmpozinybwlovcnafqfybodkhabyrglsnen"))

