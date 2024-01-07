import random                    #import the random module

user_Wallet = 200                #starting value user's "Wallet"
 
def getPoints():                 #add points if win
    global user_Wallet           #set user_Wallet in these fuctions as a global variable
    user_Wallet += 200           #user_Wallet add 200
    print("Wallet: $"+str(user_Wallet))           #print wallet amount

def losePoints():                #lose points if loss
    global user_Wallet           #same wallet variable
    user_Wallet -= 50            #wallet subtract 50
    print("Wallet: $"+str(user_Wallet))           #print wallet amount

  
while user_Wallet > 0:           #True until Wallet goes to 0
    
    userResponse = ['1','2','3','4','5','6']            #the only values the user can put in
    computer = str(random.randint(1,6))                 #random generate between 1 to 6

    user = str(None)                                    #string cast user as the input will be an int and we want to print it out

    while user not in userResponse:                     #prompts the user to keep inputting until it is within the 1-6 list
        user = input("Choose a number from 1-6: ")      #user input
     
    print("You chose: "+user)                           #print out the user's input
    print("Computer chose: "+computer)                  #print out the computer's random value
 
    if user == computer:             #if user and computer select same number
        print("You Won!!!")          #print win statement
        getPoints()                  #call getPoints function
    
    else:                            #everything else
        print("L + Bozo + Ratio")    #print loss statement
        losePoints()                 #call losePoints function
        
        
    play_again = input("Play again? (yes/no): ").lower()                #prompts the player to play again
    
    if play_again !="yes":                                              #if not yes
        you_sure = input("Are you sure you don't want to play again? You will lose all progress :( (yes/no): ").lower()  #check if tey really want to quit
        if you_sure == "no":                                            #if no (runs the entire thing again)
                print("Lets play again!")                               #print play again
        else:                    #everything else
            break                #break the while loop 


print("Bye!") #print at last when while loop breaks  
        
        
