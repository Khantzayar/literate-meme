import random


def print_signature():
    """
    Function
    -------
    Prints my student digital signature at the start of the program.
   
    Inputs
    -------
    None.

    Returns
    -------
    None.

    """
   
    print("Khant Zayar,\n400595806, Eng 1,\nENG1P13: Integrated Cornerstone Design Projects in Engineering,\nProf. Sam Scott,\nFall 2024")
def game_room(): 
    score = 0
    while True:
        
        print(f"Current Score: {score}\n\n1. Number Guess \n\n2. Modified RPSLS \n\n3. Coin Flips \n\n4. Quit")
        choice = input("\nEnter the corresponding number to select a game.")
        
        if choice == "1": 
            ## Go to Number Guess Function
            score+=play_number_guess(int(input("Guess the number rolled on 2 dices")))
            
        elif choice == "2":
            ## Go to Modified RPSLS Function
            score+=play_mrpsls(int(input("Choose One: \n1.scissors \n2.paper \n3.rock \n4.lizard \n5.spock")))
        elif choice == "3":
            ## Go to Coin Flip Function
            score += play_coin()
            
        elif choice == "4":
            #Quit the program
            print("Goodbye!")
            break
        else: 
            #invalid input
            print("Invalid Input")
        
########################'''Number Guess Game'''#######################
def play_number_guess(guess):
    cpuDiceRoll = random.randint(2, 12)
    if cpuDiceRoll == guess:
        print("\nYOU GOT IT RIGHT!! (+10 points)")
        return 10
    else:
        print("\nSorry! The dice rolled", cpuDiceRoll)
       
        if cpuDiceRoll - 4 <= guess <=cpuDiceRoll + 4 :
            if cpuDiceRoll - 2 <= guess <=cpuDiceRoll + 2:
                print("Within 2 of answer! (+5 points)")
                return 5
            else:
                print("Within 4 of answer! (+1 point)")
                return 1
           
    return 0



############## Rock,paper,scissor,lizard,spock GAME #################
def play_mrpsls(move):
    # Make a random number for each possible move the computer makes (explained in doc string)
    cpuMoveNum = random.randint(1, 5)
    cpuMoveName = ""
    if cpuMoveNum == 1:
            cpuMoveName = "scissors"
    if cpuMoveNum == 2:
            cpuMoveName = "paper"
    if cpuMoveNum == 3:
            cpuMoveName = "rock"
    if cpuMoveNum == 4:
            cpuMoveName = "lizard"
    if cpuMoveNum == 5:
            cpuMoveName = "Spock"
   
    if cpuMoveNum == move:
        print("A draw! (+5 points)")
        return 5
    elif cpuMoveNum == 1 and (move == 2 or move == 4):
        ## CPU chose scissor and you chose either paper or lizard, you lose!
        print("YOU LOSE! CPU chose scissors!")
        
    elif cpuMoveNum == 2 and (move == 5 or move == 3):
        ## CPU chose paper and you chose either rock or spock, you lose!
        print("YOU LOSE! CPU chose paper!")
        
    elif cpuMoveNum == 3 and (move == 1 or move == 4):
        ## CPU chose rock and you chose either scissor or lizard, you lose!
        print("YOU LOSE! CPU chose rock!")
        
    elif cpuMoveNum == 4 and (move == 2 or move == 5):
        ## CPU chose lizard and you chose paper or spock, you lose!
        print("YOU LOSE! CPU chose lizard!")
        
    elif cpuMoveNum == 5 and (move == 3 or move == 1):
        ## CPU chose spock and you chose either rock or scissors, you lose!
        print("YOU LOSE! CPU chose spock!")
        
    else:
        
        print("YOU WIN!! CPU chose", cpuMoveName + "! (+10 points)")
        return 10
   
    return 0


################### Coin Flip Game ######################
def play_coin():
    firstCoinFlip = random.randint(1,2)
    currentCoinFlip = random.randint(1,2)
    wins = 0
    while firstCoinFlip != currentCoinFlip:
        wins += 1
        currentCoinFlip = random.randint(1,2)
   
    if (firstCoinFlip == 1):
        print(f"Welcome to Coin Flips! Your first coin flip was heads, then you got {wins} consecutive tails which gives you +{wins*2} point(s)!")
        return wins*2
    else:
        print(f"Welcome to Coin Flips! Your first coin flip was tails, then you got {wins} consecutive heads which gives you +{wins*2} point(s)!")
        return wins*2
    


def main():
    print_signature()
    game_room()
if __name__ == "__main__":
    main()



