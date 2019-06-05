import copy

# Finds the last inversion (i, j) of a permutation with the following criteria:
# a pair (i,j) with i < j and w(i) > w(j) that maximizes i, then j
def findLastInversion(w):

  biggestI = -1
  biggestJ = -1
  
  for i in range(0, len(w)):
    for j in range(i, len(w)):
      if w[j] < w[i] and (i > biggestI or (i == biggestI and j > biggestJ)):
        biggestI = i
        biggestJ = j
  
  return (biggestI, biggestJ)

# Given a permutation and an inversion, find the pivots of the inversion
def findPivots(w, i, j):
  pivots = []

  for h in range(i - 1, 0, -1):
    if w[h] < w[j]:
      isValid = True
      for hPrime in range(h, i):
        if w[h] < w[hPrime] and w[hPrime] < w[j]:
          isValid = False
          break
      if isValid:
        pivots.append(h)
  
  return pivots

def findChildren(w, i, j, pivots):
  children = []

  for pivot in pivots:
    tmpI = w[i]
    tmpJ = w[j]
    tmpH = w[pivot]

    child = copy.deepcopy(w)
    child[pivot] = tmpJ
    child[i] = tmpH
    child[j] = tmpI
    children.append(child)

  return children

def buildTree(w):
  print("called")
  i, j = findLastInversion(w)
  pivots = findPivots(w, i, j)

  if len(pivots) == 0:
    print(w)
  else:
    children = findChildren(w, i, j, pivots)
    for child in children:
      buildTree(child)


w = [5, 4, 2, 7, 8, 3, 1, 6]
buildTree(w)