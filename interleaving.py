 
def isInterleaved(X, Y, S):
    A = X  
    B = Y
    while len(A) < len(S):
      A = A + X
    while len(B) < len(S):
      B = B + Y
    # Find lengths of the two strings 
    M = len(A) 
    N = len(B)  
    opt = [[False] * (N+1) for i in range(M+1)]
    # C can be an interleaving of A and B only of sum  
    # of lengths of A & B is equal to length of C.  
    # if ((M + N) > len(C)):  
    #     return False
    # Process all characters of A and B 
    print(A)
    print(B)
    print(S)
    for i in range(0, M+1):  
        for j in range(0, N+1): 
            if ((i + j - 1) > len(S)-1):
              break
            # two empty strings have an empty string  
            # as interleaving  
            if (i == 0 and j == 0):  
                opt[i][j] = True
  
            # A is empty  
            elif (i == 0):  
                if (B[j - 1] == S[j - 1]):  
                    opt[i][j] = opt[i][j - 1]  
              
            # B is empty  
            elif (j == 0):
                if (A[i - 1] == S[i - 1]):  
                    opt[i][j] = opt[i - 1][j]  
              
            # Current character of C matches with  
            # current character of A, but doesn't match  
            # with current character of B  
            elif (A[i - 1] == S[i + j - 1] and
                  B[j - 1] != S[i + j - 1]):  
                opt[i][j] = opt[i - 1][j]  
  
            elif (A[i - 1] != S[i + j - 1] and 
                  B[j - 1] == S[i + j - 1]):  
                opt[i][j] = opt[i][j - 1]  
  
            elif (A[i - 1] == S[i + j - 1] and 
                  B[j - 1] == S[i + j - 1]):  
                opt[i][j] = (opt[i - 1][j] or opt[i][j - 1])  
    for i in range(0, M+1):
      for j in range(0, N+1):
        print(str(opt[i][j]) + " "),
      print("\n")
    repeatX = M/len(X)
    repeatY = N/len(Y)
    for i in range (0, repeatX):
      for j in range (0, repeatY):
        if (len(S) == (i * len(X) + j * len(Y)) and opt[i*len(X)][j*len(Y)] == True):
          return True
    return False 
  
# A function to run test cases  
def test(X, Y,S):  
  
    if (isInterleaved(X, Y, S)):  
        print(S, "is interleaved of", X, "and", Y)  
    else: 
        print(S, "is not interleaved of", X, "and", Y) 
  
# Driver Code  
if __name__ == '__main__':  
    test("101", "0", "1000101011010")
