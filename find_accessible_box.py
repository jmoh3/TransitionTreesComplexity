def find_accessible_box(l):
    accessible_box = 0
    last_dominant = l[0]
    accessible_box = None
    found_inversion = False

    for i in range(1, len(l)):
        if found_inversion and l[i] - last_dominant > 0:
            print('here')
            print(last_dominant)
            accessible_box = i
        if l[i] > l[i-1]:
            found_inversion = True
            accessible_box = i
            if last_dominant > l[i-1]:
                last_dominant = l[i-1]

    return accessible_box