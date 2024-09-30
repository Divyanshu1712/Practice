# Create a function that takes two numbers as parameters and returns their sum.


arr=[1,8,7,56,90]
def largest(arr):
    max=0
    for x in arr:
        if x>max:
            max=x
    return max
print(largest(arr)) 


   