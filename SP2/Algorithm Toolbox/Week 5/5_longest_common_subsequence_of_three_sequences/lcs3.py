def lcs_of_three(X, Y, Z):
    m = len(X)
    n = len(Y)
    o = len(Z)

    L = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if X[i - 1] == Y[j - 1] == Z[k - 1]:
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1
                else:
                    L[i][j][k] = max(L[i - 1][j][k], L[i][j - 1][k], L[i][j][k - 1])

    return L[m][n][o]

n = int(input()) 
X = list(map(int, input().split()))  
m = int(input()) 
Y = list(map(int, input().split()))
l = int(input()) 
Z = list(map(int, input().split()))  

lcs_length = lcs_of_three(X, Y, Z)
print(lcs_length)