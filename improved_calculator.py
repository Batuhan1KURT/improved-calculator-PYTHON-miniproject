# TASK : BETTER CALCULATOR PROGRAM: 





import operator  # Import the 'operator' module for convenient access to arithmetic operations

def main():
    while True:  # Start an infinite loop until the user chooses to exit
        first_number = get_num_input("Enter the first number (E to exit): ")  # Get the first number from the user
        if first_number is None:  # If user chose to exit
            return  # Exit the program
        
        operator_symbol = get_operator_input()  # Get the operator from the user
        if operator_symbol is None:  # If user chose to exit
            return  # Exit the program

        second_number = get_num_input("Enter the second number (E to exit): ")  # Get the second number from the user
        if second_number is None:  # If user chose to exit
            return  # Exit the program

        try:
            result = perform_operation(first_number, operator_symbol, second_number)  # Perform the selected operation
            print(f"The result is: {result}")  # Print the result to the user
        except ValueError as e:
            print(f"Error: {e}")  # Handle value-related errors (e.g., invalid number input)
        except ZeroDivisionError:
            print("Error: Division by zero!")  # Handle division by zero error

def get_num_input(prompt):
    while True:  # Start a loop until valid input is received
        user_input = input(prompt)  # Get user input
        if user_input.lower() == "e":  # If user chose to exit
            return None  # Signal to exit
        try:
            return float(user_input)  # Convert the user input to a float (number)
        except ValueError:
            print("Error: Please enter a valid number.")  # Handle invalid number input

def get_operator_input():
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}  # Define a dictionary mapping operator symbols to corresponding functions
    while True:  # Start a loop until valid input is received
        user_input = input("Enter an operator (+, -, *, /) (E to exit): ")  # Get user input for the operator
        if user_input.lower() == "e":  # If user chose to exit
            return None  # Signal to exit
        elif user_input in operators:  # If the entered operator is valid
            return operators[user_input]  # Return the corresponding operator function
        else:
            print("Error: Invalid operator!")  # Handle invalid operator input

def perform_operation(first_num, operator_func, second_num):
    return operator_func(first_num, second_num)  # Perform the operation using the provided operator function

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
