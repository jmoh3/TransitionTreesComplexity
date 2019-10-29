def find_accessible_box(l):
    accessible_box = 0
    last_dominant = -1
    accessible_box = None
    found_inversion = False

    for i in range(1, len(l)):
        if found_inversion and l[i] - last_dominant > 0:
            accessible_box = i
        if l[i] > l[i-1]:
            found_inversion = True
            accessible_box = i
            last_dominant = l[i-1]
    
    return accessible_box

print(find_accessible_box([3, 3, 3, 7, 0, 6, 2]))

# print(find_accessible_box([4, 2, 0, 3]))