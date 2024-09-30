a = input()

even=odd = 0

for i in range(len(a)):

    seprate = int(a)%10

    a = int(a)//10

    if seprate%2 ==0:

        even +=seprate

    else:

        odd+=seprate

print(even,"",odd) 