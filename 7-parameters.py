# but functions are so much more than just allowing you to repeat code

# functions can have "parameters", which is like a variable, that can store different
# data each time you use the function
def adder(a, b):
    sum = a + b
    print(sum)

adder(2, 1) # the adder() function will find the sum, and then print it
adder(5, 3) # and we can do this with any two numbers
adder(8, 7)

# but functions can do even more!
# a function can "return" a value
def multiply(a, b):
    product = a * b
    return product

print(multiply(3, 2))