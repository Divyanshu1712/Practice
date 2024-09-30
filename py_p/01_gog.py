def check(arr1, arr2) -> bool:
    arr_1=len(arr1)
    arr_2=len(arr2)
    if arr_1 == arr_2:
        # for i in arr1:
        #     for j in arr2:
        #         arr1[i] == arr2[j]
        return True
    else:
        return False

arr1=[1,2,3,4]
arr2=[2,3,4,1]
print(check(arr1,arr2))