def linear_s(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return 1
    

arr = [2,2,5,2,4,3,4,6,7,23,33]
target = 3
linear_s(arr,target)