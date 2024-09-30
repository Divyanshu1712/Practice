# You are given a string ‘str’, the task is to check that reverses of all possible substrings of ‘str’ are present in ‘str’. If yes then the answer is 1, otherwise, the answer will be 0.

#  main string and reverse strinf equall ho toh  baat baan jaye
# n bhi add krna hai for length

main_str=input(input("enter some aplhbet"))
n=int(input("enter number"))
def reverse_str(main_str,n):
    length=len(main_str)
    new=main_str[::-1]
    if length==new:
        print("1")
    else:
        print("0")
    
        
print(reverse_str(main_str,n))


