

def sort_array(arr):
    if len(arr) < 2:
        return
    
    first_run = True
    didSwap = False
    while (first_run or didSwap):
        first_run = False
        didSwap = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                placeholder = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = placeholder
                didSwap = True