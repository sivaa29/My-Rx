def sorted_(arr):
    return sorted(x**2 for x in arr)

arr = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
output = sorted_(arr)
print(output)