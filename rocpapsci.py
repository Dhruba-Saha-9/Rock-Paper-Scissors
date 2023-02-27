import random
maxchoice =input("Enter the number of times you want to play : ")
mychoice =0
compscore =0
userscore =0
while mychoice<int(maxchoice):

 user = input("Choose one (Rock Paper or Scissors) : ").lower()
 comp = ["rock", "paper", "scissors"]
 out = random.choice(comp)

 if user not in comp:
    print("Invalid choice")
    continue

 print("You chose ", user, " and computer chose ", out)

 if user == out:
    print("Its a Tie - No Points")

 elif user == "rock":
    if out == "paper":
        print("Paper covered rock.Computer wins")
        compscore += 1
    else:
        print("Rock smashed scissors.You win")
        userscore += 1

 elif user == "scissors":
    if out == "paper":
        print("Scissors cut paper.You win")
        userscore += 1
    else:
        print("Rock smashed Scissors.Computer wins")
        compscore += 1

 elif user == "paper":
    if out == "rock":
        print("Paper covered rock.You win")
        userscore += 1
    else:
        print("Scissors cut paper.Computer wins")
        compscore += 1
 mychoice += 1

print("Your score is ", userscore, " and computer score is ", compscore)
if userscore == compscore:
    print(" No one won :| ")
elif userscore > compscore:
    print("Congratulations you win :) ")
else:
    print("Sorry, you lost but u can always try again :) ")
print("Thanks for playing")
