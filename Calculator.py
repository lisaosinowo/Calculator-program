# This program is a calculator that takes number inputs and operation symbols

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

operations = { # The operations are the keys and the functions are the values. e.g + is the key and the add() function is the value
     "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""
print(logo)
number_1 = int(input("What's the first number? "))

for symbol in operations:
    print(symbol) # This for loop prints out all of the operation symbols

calculate_again = True
while calculate_again:
    operation_symbol = input("Pick an operation from the line above. ")
    number_2 = int(input("What's the next number? "))
    calculation_function = operations[operation_symbol] # e.g operations[+] will grab the "add" function. The value of a dictionary is obtained by putting the key inside the square brackets. The operation functions are the values
    # Whatever operation function is grabbed becomes the calculation function
    answer = calculation_function(number_1, number_2) # The two numbers are used in the operation function that has been grabbed via the dictionary. A value is returned from the grabbed function which is stored into the answer variable

    print(f"{number_1} {operation_symbol} {number_2} = {answer}")


    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ") == "y":
        number_1 = answer

    else:
        calculate_again = False
        print("Goodbye!")
