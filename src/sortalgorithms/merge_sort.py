

def sort_array(arr):
    _mergesort_recursion(arr, 0, len(arr))

def _mergesort_recursion(arr, start, end):
    if end <= start + 1:
        return
    
    middle = start + int((end - start) // 2)
    _mergesort_recursion(arr, start, middle)
    _mergesort_recursion(arr, middle, end)
    _merge_sorted_subarrays(arr, start, middle, end)
    
def _merge_sorted_subarrays(arr, start, middle, end):
    i = start
    j = middle
    merged_array = []
    while (i < middle and j < end):
        if arr[i] < arr[j]:
            merged_array.append(arr[i])
            i += 1
        else:
            merged_array.append(arr[j])
            j += 1
    while (i < middle):
        merged_array.append(arr[i])
        i += 1
    while (j < end):
        merged_array.append(arr[j])
        j += 1
    for k in range(0, len(merged_array)):
        arr[start + k] = merged_array[k]

        