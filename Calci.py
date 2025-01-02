# Function to perform basic arithmetic operations
def perform_operations(num1, num2):
    # Addition
    addition = num1 + num2
    
    # Subtraction
    subtraction = num1 - num2
    
    # Multiplication
    multiplication = num1 * num2
    
    # Division
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero)"
    
    # Return the results
    return addition, subtraction, multiplication, division

# Main program
if __name__ == "__main__":
    # Accept two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform the operations
        addition, subtraction, multiplication, division = perform_operations(num1, num2)
        
        # Display the results
        print(f"\nResults:")
        print(f"Addition: {num1} + {num2} = {addition}")
        print(f"Subtraction: {num1} - {num2} = {subtraction}")
        print(f"Multiplication: {num1} * {num2} = {multiplication}")
        print(f"Division: {num1} / {num2} = {division}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")