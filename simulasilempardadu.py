import random


rolls= {}

def rolldice(min,max):
    while True:
        print("Rolling dice. . . . ")
        number=random.randint(min,max)
        if number in rolls:
            rolls[number] +=1
        else:
            rolls[number] =1
        print(f"Your Number:{number}")
        choice=input("Do you want to roll again? (y/n)")
        if choice.lower() == 'n':
            for number in range(1,7):
                print("The number", str(number), "was rolled", str(rolls[number]), "times.")
        else:
            choice= False
            
rolldice(1,6)