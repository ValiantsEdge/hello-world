'''print('Hello, world!')
inp = input('What is your name?')
print('Hello, '+inp)'''

def convertToFahrenheit(degreesCelsius):
    farh=degreesCelsius*(9/5)+32
    return farh
def convertToCelsius(degressFarhenheit):
    cel=(degressFarhenheit-32)*(5/9)
    return cel
assert convertToFahrenheit(0) == 32 
assert convertToFahrenheit(100) == 212 