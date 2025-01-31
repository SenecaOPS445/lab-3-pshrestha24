#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate'''

# Author ID: pshrestha24

def operate(number1, number2, operator):
    if operator == 'add':
        result = int(number1) + int(number2)
    elif operator == 'subtract':
        result = int(number1) - int(number2)
    elif operator == 'multiply':
        result = int(number1) * int(number2)
    else:
        result = 'Error: function operator can be "add", "subtract", or "multiply"'
    return result

if __name__ == '__main__':
    print(operate(10, 5, 'add'))       # Expected Output: 15
    print(operate(10, 5, 'subtract'))  # Expected Output: 5
    print(operate(10, 5, 'multiply'))  # Expected Output: 50
    print(operate(10, 5, 'divide'))    # Expected Output: Error Message
