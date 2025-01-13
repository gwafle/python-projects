#Grace Wafle
#11.19.2024



#Init



#Functions
#adds num1 and num2, then prints results
def add (num1, num2):
    result = num1 + num2
    print ("The result is " + str(result))

def subtract (num1, num2):
    result = num1 - num2
    print ("The result is " + str(result))

def multiply (num1, num2):
    result = num1 * num2
    print ("The result is " + str(result))


def divide (num1, num2):
    result = num1 / num2
    print ("The result is " + str(result))

#Main
i = 0
while i < 2:
    print("Welcome Preschooler to Simple Calculator")
    print("Please choose an operation:")
    print("""1. addition
    2. Subtraction
    3. Multiplication
    4. Divison
    5. Quit""")
    operation = int(input("(1-5) :"))


    if operation == 1:
        add1 = int(input(("Enter first number: ")))
        add2 = int(input(("Enter second number: ")))
        add (add1, add2)


    if operation == 2:
        sub1 = int(input(("Enter first number: ")))
        sub2 = int(input(("Enter second number: ")))
        subtract (sub1, sub2)


    if operation == 3:
        mult1 = int(input(("Enter first number: ")))
        mult2 = int(input(("Enter second number: ")))
        multiply (mult1, mult2)


    if operation == 4:
        div1 = int(input(("Enter first number: ")))
        div2 = int(input(("Enter second number: ")))
        divide (div1, div2)
    if operation == 5:
        print ("Goodbye, see you next time!")
        break



