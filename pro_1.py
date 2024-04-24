'''
problem_01
'''
#program for design a Power() function 
def Power(number , power ):
    if power == 0:
        return 1
    else:
        return (number*Power(number,power-1))
number = int(input('number : '))
power = int(input('Power : '))
result = (Power(number , power))
print(result)