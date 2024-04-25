'''
problem_2
Program for solving problem _02
Winner Winner Chocolate Dinner

'''


# function for applying the stratagey of player_01
def Player_1(to_co):

    if to_co > 0: #if there is a choclate in a bowl
        re_co = to_co -1 
        if re_co == 0:
            return 1
    else :
        return -1

    return Player_2(re_co) #calling player_2 turns with the remaining choclates in a bowl

# function for applying the stratagey of player_02
def Player_2(to_co):

    if to_co % 2 == 0 : 
        re_co = to_co-2  #if the remaining number of choclates are even player_2 picks 2 choclates
    else :
        re_co = to_co -1 #if the remaining number of choclates are odd player_2 picks 1 choclate

    return Player_1(re_co) #calling player_1 turns with the remaining choclates in a bowl

#Winner Winner Chocolate Dinner ___function for playing game
def bowl(to_co):  
        Start = Player_1(to_co)
        if Start == 1:   #checking for the return values ,if it is true player_1 wins
            print('Player 1 win !!')
            
        else:   #if it is false player_2 wins
            print('Player 2 win !!')
    
to_co = int(input('total number of chocolates in a bowl : '))
bowl(to_co)
