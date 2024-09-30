# Guessing Game: 
# A game where the user guesses a randomly generated number.


import random

def main():
    print("\nWelcome to Gussesing game!!!!!!")
    Name = input("Enter Your Name: ")
    print("\n here the things you got when you select the option.")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    
    list = [1,2,3,4,5]
    
    Num = random.choice(list)
    


if __name__ == '__main__':
    main()
