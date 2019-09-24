from reconstruct_permutation import reconstruct_permutation
from find_accessible_box import find_accessible_box

# l is our lehmer code
# p is the pivot position (remove later after we read that paper)
def get_new_lehmer_code(l, pivot):

    w = reconstruct_permutation(l)
    print(w)
    a = find_accessible_box(l)
    print(a)

    pivot_col = w[pivot]
    a_box_col = w[a]

    max_boxes = a_box_col - w[pivot]

    for idx in range(0, a):
        if w[idx] < a and w[idx] > pivot:
            max_boxes -= 1
    
    new_lehmer = l
    new_lehmer[pivot] += max_boxes
    new_lehmer[a] -= max_boxes

    return new_lehmer

print(get_new_lehmer_code([4, 2, 0, 3], 0))