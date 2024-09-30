# 4. Text-Based Adventure Game: 
# A simple game with branching storylines.


def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself at the edge of a dark forest.")
    print("Do you want to enter the forest (type 'F') or walk along the road (type 'R')?")
    
    choice = input("> ").upper()
    
    if choice == "F":
        forest()
    elif choice == "R":
        road()
    else:
        print("Invalid choice. Please type 'F' or 'R'.")
        intro()

def forest():
    print("You enter the forest and hear a strange noise.")
    print("Do you want to investigate the noise (type 'I') or keep walking (type 'W')?")
    
    choice = input("> ").upper()
    
    if choice == "I":
        investigate_noise()
    elif choice == "W":
        keep_walking()
    else:
        print("Invalid choice.")
        forest()

def road():
    print("You walk down the road and come across a village.")
    print("Do you want to enter the village (type 'E') or keep walking (type 'K')?")
    
    choice = input("> ").upper()
    
    if choice == "E":
        village()
    elif choice == "K":
        keep_walking_road()
    else:
        print("Invalid choice.")
        road()

def investigate_noise():
    print("You approach the noise and find a friendly dog. You pet the dog, and it follows you.")
    # The story can branch out further from here
    
def keep_walking():
    print("You keep walking and eventually reach a clearing. The forest seems less threatening now.")
    # More story branches

def village():
    print("You enter the village and are greeted by the locals. You find a place to rest.")
    # More story branches

def keep_walking_road():
    print("You keep walking down the road but encounter a dead end.")
    # More story branches

# Start the game
intro()
