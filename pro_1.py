'''
problem_01
'''
'''#program for design a Power() function 
def Power(number , power ):
    if power == 0:
        return 1
    else:
        return (number*Power(number,power-1))
number = int(input('number : '))
power = int(input('Power : '))
print(Power(number , power))'''


''''#program for design a Power() function 
def Power(number , power ):
    if power == 0:
        return 1
    elif power<0:
        return ('Enter only positive values for power ')
    else:
        return (number*Power(number,power-1))

number = int(input('number : '))
power = int(input('Power : '))
print(Power(number , power))'''

#program for design a Power() function 
def Power(number , power ):
    if power == 0:
        return 1
    elif power<0:
        return (1/Power(number,-power))
    else:
        return (number*Power(number,power-1))
number = int(input('number : '))
power = int(input('Power : '))
print(Power(number , power))