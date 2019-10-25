from reconstruct_permutation import reconstruct_permutation
from find_accessible_box import find_accessible_box

# l is our lehmer code
# p is the pivot position (remove later after we read that paper)
def get_new_lehmer_code(l, pivot):

    w = reconstruct_permutation(l)
    print('permutation:')
    print(w)
    a = find_accessible_box(l)
    print('a box:')
    print(a)

    pivot_col = w[pivot]
    print('pivot col:')
    print(pivot_col)

    a_box_col = w[a]

    print('a box col:')
    print(a_box_col)

    max_boxes = a_box_col - pivot_col - 1

    print('max boxes:')
    print(max_boxes)

    for idx in range(0, a):
        if w[idx] < a_box_col and w[idx] > pivot_col:
            max_boxes -= 1
    print(max_boxes)

    new_lehmer = l
    new_lehmer[pivot] += max_boxes
    new_lehmer[a] -= max_boxes

    return new_lehmer

print(get_new_lehmer_code([4, 2, 0, 3], 0))