def isSubset(arr1,arr2):
    print(f"array1: {arr1}")
    print(f"array2: {arr2}")
    # temp=arr1.copy()
    # print(f"{temp} this array is copy of arr1")
    for element in arr2:
        print(f"{element} this shows us element in arr2")
        if element in arr1:
            arr1.remove(element)
            print(f"{arr1} this array shows the subset of arr2 form arr1")
        else:
            return False
    return True


arr1=[1,2,3,4,5]
arr2=[5]
print(isSubset(arr1,arr2))
