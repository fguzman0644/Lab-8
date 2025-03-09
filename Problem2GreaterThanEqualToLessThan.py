#Fernando Guzman
#03/09/25

##Function takes two inputs from user and prints whether the sum is
##greater than 10, less than 10, or equal to 10.

inputA = float(input("Please enter one number: "))
inputB = float(input("Please enter a second number: "))

inputSum = inputA +inputB

if inputSum == 10:
    print("The sum of your two numbers is equal to 10.")
elif inputSum < 10:
    print("The sum of your two numbers is less than 10.")
else:
    print("The sum of your two numbers is greater than 10.")
