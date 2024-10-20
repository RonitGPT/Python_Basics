#==================================================================================================================
                                            # GUESSING GAME
#==================================================================================================================

import random
ans = "yes"
print("********************* WELCOME TO GUESSING GAME *********************")
name = input("ENTER YOUR NAME :- ")
print("Hello !!.... ", name ,"... Can you guess candies in the jaar ??")
print("So ",name," Guess the number between 40 to 70")
guesscounter = 0
guess = 0
num = random.randint(40,70)

while (guess != num and guesscounter < 5) :
    guess = int(input( "Guess the number "))
    guesscounter +=1
    if guess < num :
        print ("Number is higher..")
    elif guess >num:
        print ("Number is Lower..")
    else :
        print ("Congratsss !!.... You've Guessed it :) ")
if guesscounter == 5 and guess != num:
    print("OOPSS !... You are out of chances ..")
print("--------------------------------------------------------------------------------------------------------")
print("Thank you for playing :) ")






