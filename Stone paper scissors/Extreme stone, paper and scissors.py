import os
import random
import pickle



#Getting the User's name and checking if its not numeric
while True:
    
    user = str(input("Enter your NAME: ")).upper()
    os.system('cls')
    if user.isnumeric() == True:
        print("Add some letters in name.")

    if user.isalnum() == True:
        if user.isnumeric() == False:
            break
user_len = len(user)

#Checking if the user is new or old through the score list
with open('score.pickle', 'rb') as f:
    scores_data = pickle.load(f)

if scores_data.get(user) == None:
    print(f'{user}, another looser\'s name.')
else:
    print(f'Welcome back you looser {user}.')

#Starting
input("Enter to start")
os.system('cls')
print("\"s\"=STONE   \"p\"=PAPER   \"c\"=SCISSOR") 
print("Type \"EXIT\" to exit.")
print("Type \"RULES\" for rules.")
print("Type \"SCORE\" for all high scores.")
user_choose = input("ENTER to start").upper()
os.system('cls')

#The GAME

# BOT player options, points and win
options = ["s", "p", "c"]
bot_points = int(0)
def bot_wins(x):
    bot_points += 1

#user points and win
user_points = int(0)
def user_wins(x):
    user_points += 1

#Printing the results
def result(x,y,z):
    print(f'{x}     {y}     {z}')
#process
    
print(f'{user}     BOT')


while user_choose != "EXIT":

    bot_choose = random.choice(options).upper()
    user_choose = input().upper()

#Who wins and points corrections
    match user_choose:

        case _ if user_choose == "S":
            match bot_choose:
                case _ if bot_choose == "S":
                    result(user_choose, bot_choose, "tie")

                case _ if bot_choose == "P":
                    result(user_choose, bot_choose, "bot wins")

                    bot_points += 1
                    if user_points > 0:
                        user_points -= 1

                case _ if bot_choose == "C":
                    result(user_choose, bot_choose, f'{user} wins')
                    
                    user_points += 1
                    if bot_points > 0:
                        bot_points -= 1


        case _ if user_choose == "P":
            match bot_choose:
                case _ if bot_choose == "S":
                    result(user_choose, bot_choose, f'{user} wins')
                    
                    user_points += 1
                    if bot_points > 0:
                        bot_points -= 1

                case _ if bot_choose == "P":
                    result(user_choose, bot_choose, "tie")

                case _ if bot_choose == "C":
                    result(user_choose, bot_choose, f'bot wins')
                    
                    bot_points += 1
                    if user_points > 0:
                        user_points -= 1

        case _ if user_choose == "C":
            match bot_choose:
                case _ if bot_choose == "S":
                    result(user_choose, bot_choose, "bot wins")

                    bot_points += 1
                    if user_points > 0:
                        user_points -= 1

                case _ if bot_choose == "P":
                    result(user_choose, bot_choose, f'{user} wins')
                    
                    user_points += 1
                    if bot_points > 0:
                        bot_points -= 1

                case _ if bot_choose == "C":
                    result(user_choose, bot_choose, "tie")


#RULES
    if user_choose == "RULES":
        os.system('cls')
        print("Stone wins by scissors and lose by papers.")
        print("Paper wins by stone and lose by scissors.")
        print("scissors wins by paper and lose by stone.")
        print("\n Enter to go back.")
        input()
        os.system('cls')
        print(f'{user}     BOT')

#High score list
    if user_choose == "SCORE":
        os.system('cls')
        with open('score.pickle', 'rb') as f:
            scores_data = pickle.load(f)
            for name, score in scores_data.items():
                print(f"{name} : {score}")

        input("\nEnter to resume.")
        os.system('cls')
        print(f'{user}     BOT')
        

os.system('cls')
print(f'Your score: {user_points}, BOT score: {bot_points}')
input()

#saving and retrieving the scores of players with their names(id)
score_list = {user : user_points}

with open('score.pickle', 'rb') as f:
    scores_data = pickle.load(f)

if scores_data.get(user) == None:
    scores_data.update(score_list)
    

elif scores_data[user] < user_points:
    scores_data[user] = user_points
    
with open('score.pickle', 'wb') as f:
    pickle.dump(scores_data,f)
