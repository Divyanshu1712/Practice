# Create a function that returns both the area and circumference of a circle given its radius.
#  area of circle = 3.14*r*r and circumference = 2*r

import math
radius=int(input("enter radius of circle: "))

def circle(radius):
    area=math.pi*radius*radius
    circumference=2*radius*math.pi
    return(area,circumference)

a, c= circle(radius)
# print("area=",a,"circumference=",c)
print(f"area is {a:.2f} and circumfernce is {c:.2f}") # by using f we can write variable with string and this is super awsm 
# like a:.2f is minimize to 2 length when we use 3F after decimal it will to third the digit length to less like area =78.53981633974483 after this it will show like area= 12.57
print(f"when we want to show that i'm using formating function and we have to use double {{name }} like this ")

