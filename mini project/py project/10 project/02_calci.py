'''
calci app
    where we use for same as real( first we put 1 number then use opeator then use second number)
'''


def main(*args):
    num1 = int(input("Enter number: "))
    print(" choose oprators")
    choose = input("Enter herre: ")
    # while True:
    if choose == '+':
        num2 = int(input("Enter another : "))
        add = num1 + num2
        print(f"Thhe sum of {num1} and {num2} are {add}") 

    elif choose == '-':
        num2 = int(input("Enter another : "))
        sub = num1 - num2
        print(f"Thhe sub of {num1} and {num2} are {sub}")

    elif choose == '*':
        num2 = int(input("Enter another : "))
        mult = num1 * num2
        print(f"Thhe mult of {num1} and {num2} are {mult}")

    elif choose == '/':
        num2 = int(input("Enter another : "))
        div = num1 // num2
        print(f"Thhe div of {num1} and {num2} are {div}")

    else:
        print("Error")
    

if __name__ == "__main__":
    main()
