'''
problem_2
'''
#Winner Winner Chocolate Dinner
'''def bowl(co_num):
    return 
co_num = int(input('number of chocolates : '))
print(bowl(co_num))'''

def Player_1(co_num):
    co_num = co_num-1
    return Player_2(co_num)
def Player_2(co_num):
    if co_num %2==0 :
        co_num = co_num-2
        return Player_1(co_num)
    else :
        co_num = co_num-1
        return Player_1(co_num)
        
    

#Winner Winner Chocolate Dinner
def bowl(co_num):
        one = Player_1(co_num)
        if one <= 2:
            print('Player2 win')
            
        else:
            two = Player_2(co_num-1)
            if two == 1 :
                print('Player1 win')
    
co_num = int(input('number of chocolates : '))
print(bowl(co_num))