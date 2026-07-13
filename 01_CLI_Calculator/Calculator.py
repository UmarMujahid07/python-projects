def calculate(number_1, number_2, operation):
    if operation == "+":
        return number_1 + number_2
    elif operation == "-":
        return number_1 - number_2
    elif operation == "*":
        return number_1 * number_2
    elif operation == "/":
        return number_1 / number_2
    else:
        raise ValueError(f"'{operation}' is not a supported operator.")
# Main Execution
while True:
    print("\nChoose an option:")
    print("1. Perform Calculation")
    print("2. Quit Application")
    
    choice = input("Select an option (1-2): ").strip()
    if choice == "2":
        print("Exiting the system..!")
        break
    elif choice != "1":
        print("\n Invalid choice. Please enter 1 or 2.")
        continue
    try:
        
        input_1 = input("Enter first number: ").strip()
        first_number = int(input_1)
    
        input_2 = input("Enter second number: ").strip()
        second_number = int(input_2)
    
        selected_operation = input("Enter operation (+, -, *, /): ").strip()
        # Performing calculation
        result = calculate(first_number, second_number, selected_operation)
        print(f"\n[SUCCESS] Result: {result}")

    except ValueError as error_message:
        # Handles both invalid integers and invalid operations cleanly
        print(f"\n[ERROR] Invalid Input: {error_message}")

    except ZeroDivisionError:
        print("\n[ERROR] Math Error: Division by zero is not allowed.")

    finally:
        print("\nCalculation process completed.")