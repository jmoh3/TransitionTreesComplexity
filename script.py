# Finds the last inversion (i, j) of a permutation with the following criteria:
# a pair (i,j) with i < j and w(i) > w(j) that maximizes i, then j
def findLastInversion(perm):

  biggestI = -1
  biggestJ = -1
  
  for i in range(0, len(perm)):
    for j in range(i, len(perm)):
      if perm[j] < perm[i] and (i > biggestI or (i == biggestI and j > biggestJ)):
        biggestI = i
        biggestJ = j
  
  return (biggestI, biggestJ)

# Given a permutation and an inversion, find the pivots of the inversion
def findPivots(perm, i, j):
  pivots = []

  for h in range(i - 1, 0, -1):
    if perm[h] < perm[j]:
      isValid = True
      for hPrime in range(h, i):
        if perm[h] < perm[hPrime] and perm[hPrime] < perm[j]:
          isValid = False
          break
      if isValid:
        pivots.append(h)
  
  return pivots

def findChildren(perm):
  return None

w = [2, 1, 5, 4, 6, 3]

i, j = findLastInversion(w)

print(findPivots(w, i, j))