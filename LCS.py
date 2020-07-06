# # Longest Common Sequence using Recursion
# 
# def lcs(str1, str2, i, j):
#     if i == 0 or j == 0: 
#         return 0; 
#     elif str1[i-1] == str2[j-1]: 
#         return 1 + lcs(str1, str2, i-1, j-1); 
#     else: 
#         return max(lcs(str1, str2, i, j-1), lcs(str1, str2, i-1, j));
#     
# str1 = "abppplee"
# str2 = "apple"
# 
# print(lcs(str1, str2, len(str1), len(str2)))


# Longest Common Sequence using Dynamic Programming
  
def lcs(X , Y): 
    m = len(X)
    n = len(Y)
  
    L = [[None] * (n+1) for i in xrange(m+1)] 
    
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    return L[m][n] 
  
X = "abppplee"
Y = "apple"
print "Length of LCS is ", lcs(X, Y)