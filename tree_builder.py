import copy

def find_pivots(w, inversion):
  i = inversion[0]
  j = inversion[1]

  pivots = []

  for h in range(0, i):
    # first criteria for a pivot
    if w[h] < w[j]:
      valid_pivot = True
      for h_prime in range(h + 1, i):
        # second criteria for a pivot - there exists no h' with h < h' < i and w(h) < w(h') < w(j)
        if (w[h] < w[h_prime] and w[h_prime] < w[j]):
          valid_pivot = False
          break
      if valid_pivot:
        pivots.append(h)

  return pivots

permutation = [5,4,2,7,8,3,1,6]

assert find_pivots(permutation, [4, 7]) == [0, 1, 2]
assert find_pivots([2,1,5,4,6,3], [4,5]) == [0, 1]

def find_accessible_inversion(w):
  inversions = []

  for i in range(0, len(w)):
    for j in range(i + 1, len(w)):
      if w[i] > w[j]:
        inversions.append((i, j))
  
  print(inversions)

  for inversion in reversed(inversions):
    i = inversion[0]
    j = inversion[1]
    # account for zero based indexing
    # adjusted_inversion_col = inversion[1] + 1
    # j = -1

    # for idx in range(0, len(w)):
    #   if w[idx] == adjusted_inversion_col:
    #     j = idx
    
    pivots = find_pivots(w, (i, j))

    if len(pivots) > 0:
      return (i, j, pivots)

  return None

def find_children(w, i, j, pivots):
  adjusted_inversion_col = j + 1
  j_inverse = -1

  for idx in range(0, len(w)):
    if w[idx] == adjusted_inversion_col:
      j_inverse = idx
      break
  
  print("j inverse", j_inverse)

  children = []

  for pivot in pivots:
    tmp_h = w[pivot]
    tmp_i = w[i]
    tmp_j_inverse = w[j_inverse]

    child = copy.deepcopy(w)
    
    child[pivot] = tmp_j_inverse
    child[i] = tmp_h
    child[j_inverse] = tmp_i
    
    children.append(child)
  
  return children

print(find_children(permutation, 4, 7, [0, 1, 2]))

# assert find_accessible_inversion(permutation) == (4, 7, [0, 1, 2])
# assert find_accessible_inversion([2,1,5,4,6,3]) == (4, 5, [0, 1])