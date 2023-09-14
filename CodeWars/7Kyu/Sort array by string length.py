def sort_by_length(arr):
    arr.sort(key=len)
    return arr

print(sort_by_length(['beg', 'life', 'i', 'to']))