"""creating a contact book 
   where we have only Name and Contact 
   we perform some things Create, Update, Delete, Read(view) 
"""

contacts = {} # Contact Dict
favContact = {} # Addinf fav contact limit is % person only 

# main code
def main():
    
    while True:
        
        print("\n Contact Book")
        print("1. Create new Contact : ")
        print("2. Update new Contact : ")
        print("3. Delete  Contact : ")
        print("4. View  Contact : ")
        print("5. Add your FAV contact : ")
        print("6. EXIT ")
        
        # user entry what to do
        choices = input("Enter what to do: ")
        
        match(choices):
            case '1':
                """ creating new contact """
                name = input("Enter new contact name: ")
                if name in contacts:
                    print(f"Already exxist this contact:{name}")
                else:
                    age = int(input("Enter your age: "))
                    mobile = int(input(f"Enter the mobile number of contact {name}:  "))
                    contacts[name] = {
                        'age':age,
                        'mobile:':mobile
                    }
                    print("\n")
                    print("Contact add successfully!! ")
            
            case '2':
                """ update contact """
                updateName = input("Enter name to update: ")
                if updateName in contact:
                    pass
                else:
                    print("Contact not found")
            
            case '3':
                """ Delete contact """
                name = input("Enter contact name: ")
                if name in contacts:
                    del contacts[name]
                    print(f"contact {name} is deletd successfully")
                else:
                    print("conatct not found ")
                
            
            case '4':
                """ view contact """
                search_name = input("Enter contact name: ")
                if search_name in contacts:
                    found = False
                    for name, contact in contacts.items():
                        if search_name.lower() in name.lower():
                            print(f"Found- Name:{name} age:{age} mobile:{mobile}")
                            found =  True
                        else:
                            print("Not found")
                else:
                    print("Contact not found!!")
            
            case '5':
                """ add fav conatct """
                name = input("Enter fav contact name: ")
                if name in favContact:
                    print(f"Already exxist this contact:{name}")
                else:
                    age = int(input("Enter your age: "))
                    mobile = int(input(f"Enter the mobile number of contact {name}:  "))
                    favContact[name] = {
                        'age':age,
                        'mobile:':mobile
                    }
                    print("\n")
                    print("Contact add successfully!! ")

            case '6':
                """ exti code """
                exit()

            case _:
                print("Invvalid entry")
        


# Driver code
if __name__ == "__main__":
    main()
