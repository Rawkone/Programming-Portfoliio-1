print ("Choose Wisely")
sum=0
roll = input ("Do you want to roll the dice? \n")
if roll.lower() == "yes":
    import random
    number = random.randrange (1,7)
    print("Dice Roll" , number)
    sum = sum + number
    print("Total:" , sum)
elif roll.lower() == "no":
    print ("Game Over")

roll= input ("do you want to roll again?\n")
while roll.lower() == "yes":
    number = random.randrange(1,7)
    print (number)
    sum = sum + number
    print ("Total:", sum)
    roll= input ("do you want to roll again?\n")
if roll.lower() == "no":
    print ("Game Over")
    print ("Total:", sum)