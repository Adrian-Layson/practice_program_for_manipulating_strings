while True:
    # Ask user to input their full name
    name = input("Enter your full name: ").strip()

    # Check if input is not empty
    if name:
        break
    else:
        print("Invalid input. Enter your full name.")

# Count the number of characters in the input
char_count = len(name)

# Print the character count
print(f"There are {char_count} characters in your full name.")
