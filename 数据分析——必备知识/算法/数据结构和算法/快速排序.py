def partition(arr,start,end):
    i = start-1
    pivot = arr[end]
    for n in range(start, end):
        if arr[n] <= pivot:
            i += 1
            arr[i],arr[n] = arr[n],arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1
def quickSort(arr,start,end):
    if start < end:
        pi = partition(arr,start,end)
        
        quickSort(arr,start,pi-1)
        quickSort(arr,pi+1,end)