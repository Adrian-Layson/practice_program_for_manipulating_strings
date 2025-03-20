while True:
    # Ask user to input a complete statement
    statement = input("Enter your statement: ").strip()

    # Check if input is empty or invalid
    if statement:
        break
    else:
        print("Invalid input, Enter a complete statement.")

# Count the number of words in the input
# Print the number of word