import art
import calculation

print(art.logo)
print("1. +\n 2. -\n 3. *\n 4. /\n 5. ^\n 6. Square root")

running = True

operation_type = False
while calculation.calculation(operation_type) == False:
    operation_type = input("Choose mathematical operation type: ")
    first_number = float(input("Type first number: "))
    second_number = float(input("Type second number: "))

    if calculation.calculation(operation_type) == False:
        print("Wrong calculation type! Try again")

while running == True:
    result = calculation.calculation(operation_type, first_number, second_number)
    print(f"Result is: {result}")

    if result == "Nan":
        break

    running = int(input(f"Are you want to continue calculation with {result}? Type 1 to continue or 0 to end: "))

    if running == True:
        first_number = result
        operation_type = input("Choose mathematical operation type: ")
        second_number = float(input("Type second number: "))

        if calculation.calculation(operation_type) == False:
            print("Wrong calculation type! Try again")
