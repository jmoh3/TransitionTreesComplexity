import bisect

def reconstruct_permutation(l):
    w = [l[0]+1]
    sorted_w = [l[0]+1]
    
    for boxes in l[1:]:
        counter = boxes + 1
        idx = 0
        while idx < len(sorted_w) and sorted_w[idx] <= counter:
            counter += 1
            idx += 1
        to_add = counter
        w.append(to_add)
        bisect.insort(sorted_w, to_add)
    
    return w

l = [4, 2, 0, 3]
# print(reconstruct_permutation(l))