#Error handling is the process of identifying runtime errors and providing meaningful information or actions to handle them properly.

def find(numerator, denominator):
    value = numerator / denominator
    print(value)

try:
    Numerator = float(input("Enter the Numerator: "))
    Denominator = float(input("Enter the Denominator: "))

    find(Numerator, Denominator)

except ValueError:
    print("Invalid Input, Enter the number")

except ZeroDivisionError:
    print("Invalid Input, Enter the number higher than zero")

#"try" - is used to wrap code that may cause an error during execution.
#"except" - is used to catch and handle the error that occurs in the try block.

#Syntax for function with error handling:
    #function name(parameters):
    #try:
        #Input
    #catch error_name:
        #print("Error message")