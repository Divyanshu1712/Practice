# 6. Expense Tracker: 
# An app to track personal or business expenses.
# thoery 
'''
creating an app which track user expneses....
Expenses are : Rent(Home, maid cost, ), Bills(Wifi, electrcity, Gas, ), Home(Gorcery, safai ka saman ),  daily(like- chai, snack, auto), mislleanoues(mobile recharge, online food, )

'''
app = {} 

def Home():
    print(" ADD your expense in Home CAto: when you done write exit ")
    
    while True:
        add = input("Enter you expense name ").upper()

        if add == 'EXIT': 
            break
        
        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("invalid entry!")
            continue
            
        app['Home'] = {
            'Expense': add,
            'Amount': amount
        } 
    print("Expenese add succesfully!!")
    return main()


def Rent():
    print(" ADD your expense in Rent CAto: when you done write exit ")
    
    while True:
        add = input("Enter you expense name ").upper()
        if add == 'EXIT': 
            break 

        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("invalid entry!")
            continue
        
        app['Rent'] = {
            'Expense': add,
            'Amount': amount
        }

        print("Expenese add succesfully!!")
    
    return main()  

def Bills():
    
    print(" ADD your expense in Bills CAto: when you done write exit ")
    
    while True:
        add = input("Enter you expense name ").upper()

        if add == 'EXIT': 
            break 

        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("invalid entry!")
            continue

        app['Bills'] = {
            'Expense': add,
            'Amount': amount
        } 
        print("Expenese add succesfully!!")
    # print(app) 
    return main()

def Miscellaneous():
    
    print(" ADD your expense in Miscellaneous CAto: when you done write exit ")
    
    while True:

        add = input("Enter you expense name ").upper()

        if add == 'EXIT': 
            break 

        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("invalid entry!")
            continue

        app['Miscellaneous'] = {
            'Expense': add,
            'Amount': amount
        } 
    print("Expenese add succesfully!!")
    # print(app)
    return main()

def view():
    load_data = app

    print(load_data)
    
    return main()


def main():
    print("\n Expense Tracker.")
    print("1. HOME")
    print("2. Rent")
    print("3. Bills")
    print("4. mislleanoues")
    print("5. View ")
    print("6. Exit")

    choose = input("choose cateogry to add: ")

    match choose:
        case '1':
            Home()
        case '2':
            Rent()
        case '3':
            Bills()
        case '4':
            Miscellaneous()
        case '5':
           view()
        case '6':
            exit()
        case _:
            print("Invalid!!")
            main()


if __name__ == '__main__':
    main()
