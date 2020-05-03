import argparse
import sys
# Global vairable used for trace output runs
numComparisions = 0

#
#@Brief - Will determine if S is an interleaving of
# strings X and Y
#
#@Param[in] X - One of the potential interleaving strings
#@Param[in] Y - One of the potential interleaving strings
#@Param[in] S - The main string to determine if the string is 
# interleaving
#
#@Return bool - True if S is an interleaving of X and Y
# false otherwise
#
def isInterleaved(X, Y, S):
    #Need at least 2 of X and Y for this to be true
    global numComparisions
    if len(S) < 2*(len(X) + len(Y)):
      return False
    A = X
    B = Y
    while len(A) < len(S):
      A = A + X
    while len(B) < len(S):
      B = B + Y
    M = len(A)
    N = len(B)
    opt = [[False] * (N+1) for i in range(M+1)]
    for i in range(0, M+1):
        numComparisions = numComparisions + 1
        for j in range(0, N+1):
            numComparisions = numComparisions + 1
            if ((i + j - 1) > len(S)-1):
              break
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
            elif (A[i - 1] == S[i + j - 1] and B[j - 1] != S[i + j - 1]):
              opt[i][j] = opt[i - 1][j]
            elif (A[i - 1] != S[i + j - 1] and B[j - 1] == S[i + j - 1]):
              opt[i][j] = opt[i][j - 1]
            elif (A[i - 1] == S[i + j - 1] and
              B[j - 1] == S[i + j - 1]):
              opt[i][j] = (opt[i - 1][j] or opt[i][j - 1])
    repeatX = M/len(X)
    repeatY = N/len(Y)
    for i in range (0, repeatX):
      for j in range (0, repeatY):
        if (len(S) == (i * len(X) + j * len(Y)) and opt[i*len(X)][j*len(Y)] == True):
          return True
    return False 

#
#@Brief sets up the inputs and trace writing for the program
#Will create and write trace output to the results folder.
#
#@param[in] arg - Name of the input file to parse
#
#@return void

def test(arg):
    f=open(str(arg), "r")
    lines = f.read()
    f.close()
    global numComparisions
    r=open("results/results.txt", "w+")
    st = lines.split()
    X = st[0]
    Y = st[1]
    S = st[2]
    r.write("X string: " + X + " Y string: " + Y + " S string: " + S + "\n")
    r.write("The length of S is: " + str(len(S)) + "\n")
    print("The length of S is: " + str(len(S)) + "\n")
    if (isInterleaved(X, Y, S)):
        r.write(S+ " is interleaved of "+ X + " and "+ Y + "\n")
        print(S, "is interleaved of", X, "and", Y)
    else:
        r.write(S + " is not interleaved of " +  X + " and " + Y + "\n")
        print(S, "is not interleaved of", X, "and", Y)
    r.write("Total number of comparisons is: "  + str(numComparisions) + "\n")
    r.close() 
    print("Trace run results are in results/results.txt")
parser = argparse.ArgumentParser()
parser.add_argument("-il", help="Determines if string is an interleaving of two other strings", type=test, action="store")

if len(sys.argv) <= 1:
  sys.argv.append('--help')

options = parser.parse_args()
