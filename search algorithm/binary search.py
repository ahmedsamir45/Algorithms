def BinarySearch(list1, value):
    low = 0
    high = len(list1)-1
    while low <= high:
        mid = (low+high)//2
        if list1[mid] > value: high = mid-1
        elif list1[mid] <value: low= mid+1
        else: return mid
    return -1
A =[1534,246,933, 127,277,321,454,565,2201]
print(BinarySearch(A,277))