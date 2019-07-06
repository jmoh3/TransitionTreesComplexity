import numpy as np
import copy

BLANK_SPACE = 0
DOT = 1
LINE = 2
DOMINANT_COMPONENT = 3

# builds the rothe diagram for a permutation w
def build_rothe_diagram(w):
  diagram = np.zeros((len(w), len(w)))

  for i in range(0, len(w)):
    diagram[i][w[i] - 1] = DOT
    # horizontal line next to dot
    for j in range(w[i], len(w)):
      diagram[i][j] = LINE
    # vertical line next to dot
    for k in range(i + 1, len(w)):
      diagram[k][w[i] - 1] = LINE
    
  diagram[0][0] = 3

  for i in range(0, len(w)):
    for j in range(0, len(w)):
      if diagram[i][j] != 0 and not (i == 0 and j == 0):
        break
      if i == 0 or diagram[i - 1][j] == 3:
        diagram[i][j] = 3

  return diagram

def find_accessible_box(rothe):
  accessible_box = (0, 0)

  ess = build_essential_set(rothe)

  if is_vexilliary(rothe, ess) or len(ess) == 0:
    return None

  accessible_box = (0, 0)

  for elem in ess:
    if elem[2] != 3:
      if accessible_box == (0, 0):
        accessible_box = (elem[0], elem[1])
      if elem[0] > accessible_box[0] or (elem[0] == accessible_box[0] and elem[1] > accessible_box[1]):
        accessible_box = (elem[0], elem[1])
  
  return accessible_box

# this is broken (I think)
def find_pivots(rothe, accessible_box):
  pivots = []

  for i in range(0, accessible_box[0]):
    for j in range(0, accessible_box[1]):
      if rothe[i][j] == DOT:
        pivots.append((i, j))
  
  return pivots

def find_children(w, rothe):
  accessible_box = find_accessible_box(rothe)

  if accessible_box == None:
    return []

  pivots = find_pivots(rothe, accessible_box)

  i = accessible_box[0]
  j = -1

  # find inverse of accessible box's column
  for idx in range(0, len(w)):
    # must adjust by 1 because of 0 based indexing
    if w[idx] == accessible_box[1] + 1:
      j = idx
      break

  if len(pivots) == 0:
    return list()

  children = []

  for pivot in pivots:
    child = copy.deepcopy(w)

    h = pivot[0]

    w_h = w[h]
    w_i = w[i]
    w_j = w[j]

    child[h] = w_j
    child[i] = w_h
    child[j] = w_i

    children.append(child)

  return children

def build_tree(w):
  rothe = build_rothe_diagram(w)

  children = find_children(w, rothe)

  if len(children) == 0:
    print(w)
  else:
    for child in children:
      build_tree(child)

def build_essential_set(rothe):
  essential_set = []

  for i in range(0, len(rothe) - 1):
    for j in range(0, len(rothe) - 1):
      is_box = rothe[i][j] == BLANK_SPACE or rothe[i][j] == DOMINANT_COMPONENT
      is_southwest = (rothe[i + 1][j] != BLANK_SPACE and rothe[i + 1][j] != DOMINANT_COMPONENT) and (rothe[i][j + 1] != BLANK_SPACE and rothe[i][j + 1] != DOMINANT_COMPONENT)
      
      if is_box and is_southwest:
        if (rothe[i][j] == BLANK_SPACE):
          essential_set.append((i, j, BLANK_SPACE))
        else:
          essential_set.append((i, j, DOMINANT_COMPONENT))
  
  return essential_set

def is_vexilliary(rothe, essential_set):

  for idx in range(0, len(essential_set)):
    elem = essential_set[idx]
    i = elem[0]
    j = elem[1]

    for idx_b in range(idx + 1, len(essential_set)):
      to_compare = essential_set[idx_b]

      if is_strictly_northwest(elem, to_compare) or is_strictly_northwest(to_compare, elem):
        return False
  
  return True

       
# checks if a = (i_1, j_2) is northwest of b = (i_2, j_2)
def is_strictly_northwest(a, b):
  if a[0] < b[0] and a[1] < b[1]:
    return True
  return False

w = [5,4,2,7,8,3,1,6]

build_tree(w)

# rothe = build_rothe_diagram(w)

# ess = build_essential_set(rothe)

# print(is_vexilliary(w, ess))

# build_tree([5, 6, 2, 7, 4, 3, 1, 8])