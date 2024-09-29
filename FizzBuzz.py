#Write a program that prints the numbers 1 to 50. But, for multiples of 3, print "Fizz" instead of the number
# For multiples of 5, print "Buzz". For the numbers which ar multiples of both 3 and 5, print "FizzBuzz"


def fizzbuzz():
    for number in range(1,51):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else: 
            print(number)

#Write a Python function that takes a string as an input and returns the string reversed

def string_reverse(w):
    #Note slicing with [start:stop:step]
    return w[::-1]
    
#Write a function that takes a positive integer as input and returns the sum of its digits


