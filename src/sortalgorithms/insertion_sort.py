
def sort_array(arr):
    for sorted_portion_index in range(0, len(arr)):
        next_min = arr[sorted_portion_index]
        min_index = sorted_portion_index
        for j in range(sorted_portion_index + 1, len(arr)):
            if arr[j] < next_min:
                next_min = arr[j]
                min_index = j
                
        arr[min_index] = arr[sorted_portion_index]
        arr[sorted_portion_index] = next_min