def lcs(X, Y):
    m = len(X)
    n = len(Y)

    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    length_of_lcs = L[m][n]

    

    return length_of_lcs

n = int(input())  
X = list(map(int, input().split()))  
m = int(input())  
Y = list(map(int, input().split()))  

lcs_length = lcs(X, Y)
print(lcs_length)