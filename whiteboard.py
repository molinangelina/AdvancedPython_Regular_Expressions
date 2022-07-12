#Fizz Buzz
#Given a random number as an input to a function, return "FIZZ" if the number is even and "BUZZ" if the number is odd
#def num(x):
#    if x % 2 == 0:
#        return 'fizz'
#    elif x % 2 == 1:
#        return 'buzz'

#print(num(5))

#Fizz Buzz #2
#Write a function to print all numbers 1 to n, but there are some constraints
#If the number is divisible by 3, print ‘Fizz’ instead of the number
#If the number is divisible 5, print ‘Buzz’ instead of the number
#If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
#Otherwise, simply print the number

def num(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'fizzbuzz'
    elif x % 3 == 0:
        return 'fizz'
    elif x % 5 == 1:
        return 'buzz'
    else:
        return x

print(num(15))