import random
print("Welcome to Stone Paper Scissors game:\n"
      +"The rules for these are very simple..let me introduce:\n"
      +"Player 1:Rock :: Player 2:Paper--->> Player 2 Wins \n"
      +"Player 1:Rock :: Player 2:Scissor--->> Player 1 Wins \n"
      +"Player 1:scissor :: Player 2:Paper--->> Player 1 Wins \n"
      +"Ok, now lwts start the game:")
while True:
    print("Player 1, Please enter your choice:) \n"
          +"Choice 1:Rock\n"
          +"Choice 2:Paper\n"
          +"Choice 3:Scissor")
    choice=int(input("Enter here please:"))
    while choice>3 or choice<1:
        choice=int(input("Please enter a valid input."))
    if choice==1:
        player1_choice="Rock"
    if choice==2:
        player1_choice="Paper"
    if choice==3:
        player1_choice="Scissor"
    print("The player1's choice is:"+player1_choice)
    print("Now, it's time for player2's choice:")
    choice2=random.randint(1,3)
    if choice2 == 1:
        player2_choice = "Rock"
    if choice2 == 2:
        player2_choice = "Paper"
    if choice2 == 3:
        player2_choice = "Scissor"
    print("The player2's choice is:" + player2_choice)
    print("Player 1 V/s Player 2")
    if choice==choice2:
        result="Draw"
    if choice==1 and choice2==2:
        result="Player2"
    if choice==1 and choice2==3:
        result="Player1"
    if choice==2 and choice2==1:
        result="Player1"
    if choice==2 and choice2==3:
        result="Player2"
    if choice==3 and choice2==1:
        result="Player2"
    if choice==3 and choice2==2:
        result="Player1"
    if result=="Draw":
        print("It's a Tie")
    if result=="Player1":
        print("Player1 Wins")
    if result=="Player2":
        print("Player2 Wins")
    print("DO you want to play again?? (Y/N):")
    ans=input()
    if ans=="N":
        break
print("Thanks for Playing,, :)")