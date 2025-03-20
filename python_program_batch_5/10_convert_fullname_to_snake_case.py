while True:
    # Ask user to input their full name in incorrect casing
    name = input("Enter your full name (incorrect casing): ").strip()

# Check if input is empty or invalid
    if name:
        break
    else:
        print("Invalid input. Enter your full name.")

# Convert to snake case
# Print the name in snake case