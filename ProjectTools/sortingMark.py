def quick_sort(arr):
    left = []
    right = []
    equal = []

    if len(arr) > 1:
        y = arr[-1]
        for x in arr:
            if x < y:
                left.append(x)
            elif x == y:
                equal.append(x)
            elif x > y:
                right.append(x)
        return quick_sort(left) + equal + quick_sort(right)
    else:
        return arr