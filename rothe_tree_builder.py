import numpy as np
import copy

BLANK_SPACE = 0
DOT = 1
LINE = 2
DOMINANT_COMPONENT = 3

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

  for i in range(0, len(rothe)):
    for j in range(0, len(rothe)):
      if rothe[i][j] == 0 and (i > accessible_box[0] or (i == accessible_box[0] and j > accessible_box[1])):
        accessible_box = (i, j)
  
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
  pivots = find_pivots(rothe, accessible_box)
  print(accessible_box, pivots)

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
  # print(w)
  rothe = build_rothe_diagram(w)
  # print(rothe)
  # if w == [5, 6, 2, 7, 4, 3, 1, 8]:
  #   print("HERE+++++")
  children = find_children(w, rothe)
  # if w == [5, 6, 2, 7, 4, 3, 1, 8]:
  #   print(children)

  # return
  if len(children) == 0:
    print(w)
  else:
    for child in children:
      build_tree(child)

w = [5,4,2,7,8,3,1,6]

# print(build_rothe_diagram(w))

build_tree(w)

# new_w = [6, 4, 2, 7, 5, 3, 1, 8]

# build_tree(new_w)