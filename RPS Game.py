import random as rm
def scorecard(n,c):
    user_points = 0
    computer_points = 0
   
    if(n==rock and c==paper or n==paper and c==scissor or n==scissor and c==rock):
        print("Computer Wins\nComputer Choice:-", c)
        computer_points += 1
    elif n==c:
        print("Tied\nComputer Choice:-", c)
        computer_points += 0
        user_points +=0
    else:
        print("You Win\nComputer Choice:-", c)
        user_points +=1
        
    print("User Points:", user_points)
    print("Computer Points:", computer_points)
    return user_points, computer_points
    
while True:
    n=(input("Select your choice (rock,paper,scissor): "))
    print("Your Choice:", n)
    rock="rock"
    paper="paper"
    scissor="scissor"
    c=computer_number = rm.randint(1,3)
    if c ==1:
        c="rock"
    elif c ==2:
        c="paper"
    else:
     c="scissor"
    user_points, computer_points=scorecard(n,c)
    play_again=input("Do you wanna play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
scorecard()