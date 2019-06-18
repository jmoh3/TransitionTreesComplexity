import copy

# Finds the last inversion (i, j) of a permutation with the following criteria:
# a pair (i,j) with i < j and w(i) > w(j) that maximizes i, then j
def findLastInversion(w):

  inversions = []
  
  for i in range(0, len(w)):
    for j in range(i, len(w)):
      if w[j] < w[i]:
        inversions.append((i, j))

  # Loop backwards through inversions (guarantees maximum i, then maximum j)
  for inversion in reversed(inversions):
    i, j = inversion[0], inversion[1]

    # TODO: find the inverse of j HERE
    j_inverse = -1
      
    for idx in range(0, len(w)):
      if w[idx] == j + 1:
        j_inverse = idx
        break
    j = j_inverse

    pivots = findPivots(w, i, j)

    # First inversion with pivots
    if len(pivots) != 0:
      return i, j_inverse, pivots

  # No accessible inversion found
  return None

# Given a permutation and an inversion, find the pivots of the inversion
def findPivots(w, i, j):
  pivots = []

  for h in range(0, i):
    if w[h] < w[j]:
      isValid = True
      # ensure that all h' (h < h' < i ) satisfies w(h) < w(h') < w(j)
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
    tmpH = w[pivot]
    tmpI = w[i]
    tmpJ = w[j]

    child = copy.deepcopy(w)
    
    child[pivot] = tmpJ
    child[i] = tmpH
    child[j] = tmpI
    
    children.append(child)

  return children

def buildTree(w):
  try:
    # Will throw an exception if no pivots are found
    i, j, pivots = findLastInversion(w)

    children = findChildren(w, i, j, pivots)

    for child in children:
      buildTree(child)
      print("child:", child)
  except:
    # w is vexilliary, leaf has been reached
    print(w)

w = [5,4,2,7,8,3,1,6]
buildTree(w)