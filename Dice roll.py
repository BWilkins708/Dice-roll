from random import randint

def rand():
    return randint(1,6)
    
repeat = True
while repeat:
    print("You rolled",rand())
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()
print("Dice roll stopped")
