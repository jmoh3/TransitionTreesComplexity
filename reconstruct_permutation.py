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

def reconstruct_permutation_complete(l):
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
    
    last = 1

    for idx in range(0, len(sorted_w)):
        if last < sorted_w[idx]:
            while last < sorted_w[idx]:
                w.append(last)
                last += 1
        if sorted_w[idx] == last:
            last += 1

    return w

print(reconstruct_permutation_complete([5, 2, 0, 2]))