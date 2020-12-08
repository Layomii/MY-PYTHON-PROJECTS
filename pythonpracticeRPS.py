from random import raindint


#list of options
game = ["Rock","Paper", "Scissors"]


#set computer choice
computer = game[raindaint(o,1)]



#set points variable and values
playersPoint = 0
computersPoint = 0
goOn = True


while goOn:
 #allow user input
    player = (" Enter Rock, Paper, Scissors? or enter Finish to end!/n")
    if player = "Finish"
    goOn = Finish
    elif: player = "computer"
    print("Tie")
    elif player == "Rock":
        if computer = "Paper"
        print("You Lose!", computer, "covers", player)
        computersPoint = computersPoint + 1
        else:
            print("You Win", player, "smashes",computer)
            elif player == "paper":
                if computer == "Scissors"
                print("You Lose", computer, "cuts", player)
                computersPoint = computersPoint + 1
                else:
                    print("You Win", player, "covers", computer)
                    elif player == "Scissors":
                        if computer == "Rock"
                        print("You Lose...", computer, "smashes", player)
                        computersPoint = computersPoint + 1
                        else:
                            print("You Win", player, "cut", computer)
                            else:
                                print("That is not a valid choice". "Try again!")
#assigning options to computer again
computer = game[randint(0,2)]
    print('********Next Turn********')

#Printing final points
print("********Final Points********")
print("Player: ", playersPoint)
print("Computer: ", computersPoint)
