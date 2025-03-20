while True:
    # Ask user to input their full name in incorrect casing
    name = input("Enter your full name (incorrect casing): ").strip()

    # Check if input is empty or invalid
    if name:
        break
    else:
        print("Invalid input. Enter your full name.")

# Convert to pascal case
pascal_case_name = ''.join(word.capitalize() for word in name.split())

# Print the name in pascal case
print(pascal_case_name)