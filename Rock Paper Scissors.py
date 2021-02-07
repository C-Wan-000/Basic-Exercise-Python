import random

robot = random.randint(0,2)

me = input("Please enter Scissors(0),Rock(1),Paper(2):")

#Scissors
if me==str(0) :
    int(me)
    print("Your input is Scissors(0)")
    if robot == 0 :
        print("The randomly generated number is (%d)Scissors"%robot)
        print("This is a draw.")
    elif robot == 1 :
        print("The randomly generated number is (%d)Rock"%robot)
        print("You lose.")
    elif robot == 2 :
        print("The randomly generated number is (%d)Paper"%robot)
        print("Congratulations,you won.")
#Rock
elif me==str(1) :
    int(me)
    print("Your input is Rock(1)")
    if robot == 0 :
        print("The randomly generated number is (%d)Scissors"%robot)
        print("Congratulations,you won.")
    elif robot == 1 :
        print("The randomly generated number is (%d)Rock"%robot)
        print("This is a draw.")
    elif robot == 2 :
        print("The randomly generated number is (%d)Paper"%robot)
        print("You lose.")
#Paper
elif me==str(2) :
    int(me)
    print("Your input is Paper(2)")
    if robot == 0 :
        print("The randomly generated number is (%d)Scissors"%robot)
        print("You lose.")
    elif robot == 1 :
        print("The randomly generated number is (%d)Rock"%robot)
        print("Congratulations,you won.")
    elif robot == 2 :
        print("The randomly generated number is (%d)Paper"%robot)
        print("This is a draw.")
else :
    print("Your input is incorrect and the program exits.")
