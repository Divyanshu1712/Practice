# Write a function that greets a user. If no name is provided, it should greet with a default name.
# "HELLO{name},Good morning" agar naam nhi hai toh default name print krwa do 


def greet(name="user"):
    return "namsate"+" "+name+ " " +"kese ho ji sexy lg rhe"

name=input("Enter name: ")
print(greet(name))