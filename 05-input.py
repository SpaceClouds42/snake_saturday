# most applications need a user to input some information,
# or even track key presses to move a character..

my_input = input("Hi! What's your name? ")
print("Nice to meet you,", my_input)

# using the last example, we can add user input for setting `a` and `b`
a = int(input("a: ")) # we use int() around the input to convert the data to a number
b = int(input("b: ")) # notice: if we try a = "1", a + 1 will error. "1" is a string

sum = a + b
difference = a - b
product = a * b
quotient = a / b

print("a + b =", sum)
print("a - b =", difference)
print("a * b =", product)
print("a / b =", quotient)